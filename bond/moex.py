from bond.models import *
from bond.bond_yield import get_yield_xirr
import json
import requests
from datetime import datetime, timedelta, date

from django.db.models import Q


def add_emitter(bond):
    if bond.emitter is not None:
        return

    bond.emitter = Emitter.objects.get_or_create(moex_id=bond.moex_id)[0]
    bond.save()


def get_all_bonds():
    """
    Getting all bonds from moex-api.
    Saving such parameters as isin, title, moex_id, trading board, emitter, emitter inn.
    """
    st = 0
    while True:

        url = \
            f'https://iss.moex.com/iss/securities.json?group_by=group&group_by_filter=stock_bonds&limit=100&start={st}'
        st += 100
        j = json.loads(requests.get(url).text)
        if len(j["securities"]["data"]) == 0:
            break
        for item in j["securities"]["data"]:
            if len(item) > 8 and item[6] == 1:
                bond = Bond.objects.get_or_create(isin=item[1])[0]
                bond.title = item[4]
                bond.moex_id = item[7]
                bond.board = item[-2]
                bond.save()
                add_emitter(bond)
                if item[9] is not None and bond.emitter.inn is None:
                    bond.emitter.inn = int(item[9])
                    bond.emitter.save()


# !!!!!!!!! Delete if everything is OK
def add_emitters():
    """
    Create emitters of existing bonds.

    TO DO: find out why I still need if because all emitters are created in get_all_bonds

    """
    for bond in Bond.objects.filter(moex_id__isnull=False, emitter__isnull=True):
        try:
            if bond.moex_id is not None and bond.emitter is None:  # TO DO: why I need because of filter of for
                bond.emitter = Emitter(moex_id=bond.moex_id)
                bond.save()
        except Exception as ex:
            print(bond.isin, bond.moex_id, ex)


def get_prices():
    boards = Bond.objects.all().values('board').distinct()
    for i in boards:
        board = i["board"]
        url = f'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/{board}/securities//.json'
        j = json.loads(requests.get(url).text)
        for b in j["securities"]["data"]:
            isin = b[0]
            if b[8] is None:
                continue
            try:
                bond = Bond.objects.get(isin=isin)
                bond.price = float(b[8])
                bond.save()
            except:
                pass


def delete_without_prices():
    Bond.objects.filter(price__isnull=True).delete()


def get_moex_info(update_all_bonds=True):
    """
    Getting from moex-api info about issue date, maturity date, facevalue, currency, volume, coupon, end date
    and is for qualified investors.

    :return:
    """
    cnt = 0
    size = Bond.objects.all().count()
    for bond in Bond.objects.all():
        cnt += 1
        if bond.coupon is not None and update_all_bonds == 0:
            continue
        print('get_moex_info', bond.isin, cnt, f'/ {size}')
        try:
            url = f'https://iss.moex.com/iss/securities/{bond.isin}/.json'
            j = json.loads(requests.get(url).text)
            if len(j['description']['data']) > 0:
                for item in j['description']['data']:
                    if item[0] == 'ISSUEDATE' and item[2] is not None:
                        bond.placement_date = item[2]
                    elif item[0] == 'MATDATE' and item[2] is not None:
                        bond.maturity_date = item[2]
                    elif item[0] == 'INITIALFACEVALUE' and item[2] is not None:
                        bond.start_facevalue = float(item[2])
                    elif item[0] == 'FACEUNIT' and item[2] is not None:
                        bond.currency = Currency.objects.get_or_create(title=item[2])[0]
                    elif item[0] == 'ISSUESIZE' and item[2] is not None:
                        bond.issue_volume = int(item[2])
                    elif item[0] == 'FACEVALUE' and item[2] is not None:
                        bond.facevalue = float(item[2])
                    elif item[0] == 'COUPONVALUE' and item[2] is not None:
                        bond.coupon = Coupon.objects.create(size=float(item[2]), aci=0, period=0)
                    elif item[0] == 'ISQUALIFIEDINVESTORS' and item[2] == '1':
                        bond.is_for_qualified_investors = 1
                    elif item[0] == 'BUYBACKDATE' and item[2] is not None:
                        bond.end_date = item[2]

                bond.save()
        except Exception as ex:
            print('Ошибка get_moex_info', bond.isin, ex)


def update_coupons():
    """
    Getting data about coupons from moex-api.
    :return:
    """
    url = 'https://iss.moex.com/iss/engines/stock/markets/bonds/securities//.json'
    j = json.loads(requests.get(url).text)
    for item in j['securities']['data']:
        if Bond.objects.filter(isin=item[0]).exists():
            bond = Bond.objects.get(isin=item[0])

            if bond.coupon is not None:
                bond.coupon.aci = float(item[7])
                bond.coupon.period = int(item[15])
                bond.coupon.save()

                if bond.coupon.size is None or bond.coupon.period is None or bond.coupon.period == 0:
                    continue
                bond.coupon.sum = bond.coupon.size * round(365 / bond.coupon.period, 0)
                bond.coupon.save()


def parse_amortizations(bond, j):
    flag = 0
    for item in j['amortizations']['data']:
        flag = 1
        for i in range(len(item)):
            if item[i] is None:
                item[i] = 0
        p = Payment(date=item[3], bond=bond, size=float(item[8]), relative_size=float(item[7]),
                    currency=Currency.objects.get_or_create(title=item[6])[0],
                    type=PaymentType.objects.get_or_create(title='Амортизация')[0])
        p.save()
    return flag


def parse_coupons(bond, j):
    flag = 0
    for item in j['coupons']['data']:
        flag = 1
        for i in range(len(item)):
            if item[i] is None:
                item[i] = 0
        p = Payment(date=item[3], bond=bond, size=float(item[9]), relative_size=float(item[10]),
                    currency=Currency.objects.get_or_create(title=item[8])[0],
                    type=PaymentType.objects.get_or_create(title='Купон')[0])
        p.save()
    return flag


def parse_offers(bond, j):
    flag = 0
    for item in j['offers']['data']:
        flag = 1
        for i in range(len(item)):
            if item[i] is None:
                item[i] = 0
        p = Payment(date=item[3], bond=bond, size=0, relative_size=0,
                    currency=Currency.objects.get_or_create(title=item[7])[0],
                    type=PaymentType.objects.get_or_create(title=item[11])[0])
        p.save()
    return flag


def add_payments(upd_all=0):
    """
    Getting all payments such as coupons, offers and amortizations from moex-api.

    :param upd_all: = 1, if we should update all bonds, 0 if we should update only new ones.
    :return:
    """
    cnt = 0
    num = Bond.objects.all().count()
    for bond in Bond.objects.all():
        cnt += 1

        if bond.payment_set.count() != 0 and upd_all == 0:
            continue
        print('add_payments', cnt, '/', num)
        try:
            start = 0
            bond.payment_set.all().delete()
            flag = 1
            while flag:

                url = f'https://iss.moex.com/iss/securities/{bond.isin}/bondization.json?&start={start}'
                j = json.loads(requests.get(url).text)
                flag = parse_amortizations(bond, j) + parse_coupons(bond, j) + parse_offers(bond, j)

                start += 20

            if not bond.payment_set.filter(~Q(type__id=2), date=bond.end_date).exists():
                p = Payment(date=bond.end_date, bond=bond, size=0, relative_size=0,
                            currency=bond.currency,
                            type=PaymentType.objects.get_or_create(title='Оферта/Опцион')[0]
                            )
                p.save()

        except Exception as ex:
            print('Error add_payments', bond.isin, ex)


def change_100_amortization():
    for payment in Payment.objects.all():
        if abs(payment.relative_size - 100) < 0.01:
            payment.type = PaymentType.objects.get(title='Погашение')
            payment.save()


def get_liquidity_month():
    """
    Calculating liquidity as average trading volume for last 30 days.
    :return:
    """
    num = Bond.objects.all().count()
    smth = 0
    for bond in Bond.objects.all():
        smth += 1
        print('get_liquidity_month', smth, '/', num)
        date = datetime.today().date() - timedelta(days=30)
        url = \
            f'https://iss.moex.com/iss/history/engines/stock/markets/bonds/sessions/3/securities/{bond.isin}/.json' \
            f'?iss.meta=off&iss.only=history&from={date}'
        j = json.loads(requests.get(url).text)
        cnt = 0
        for item in j['history']['data']:
            cnt += item[5]
        if len(j['history']['data']) > 0:
            bond.liquidity = int(cnt // len(j['history']['data']))
            bond.save()
        else:
            bond.liquidity = 0
            bond.save()


def get_end_date():
    """
    Calculating buyback date from payments.
    :return:
    """
    for bond in Bond.objects.all():
        try:
            bond.end_date = bond.maturity_date
            payments = Payment.objects.filter(bond=bond).order_by('date', '-type_id')
            now = datetime.now().date()
            if len(payments) > 0:
                for p in payments:
                    if p.date <= now:
                        continue
                    if p.type_id in [3, 4, 6, 7, 8, 9]:
                        bond.end_date = p.date
            bond.save()
        except Exception as ex:
            print('error get_end_date', bond.isin, ex)


def fix_aci():
    """
    Fixing bug with aci in foreign currencies, because in such cases moex-api gives aci in rubles.
    :return:
    """
    today = datetime.today().date()
    for bond in Bond.objects.filter(coupon__isnull=False):
        if bond.coupon.aci > bond.coupon.size:
            try:
                aci = (bond.coupon.period - (bond.payment_set.filter(date__gte=today).order_by(
                    "date").first().date - today).days) / bond.coupon.period * bond.coupon.size
                bond.coupon.aci = aci
                bond.coupon.save()
            except Exception as ex:
                print(bond.isin, ex)


def fast_update():
    """
    Updating only prices and yields of bonds.
    :return:
    """
    get_prices()
    delete_without_prices()
    update_coupons()
    fix_aci()
    get_yield_xirr()


def update_all_bonds(moex_info=0, payments=0):
    """
    Updating all bonds data.
    :param moex_info: 1 if we want to update moex_info for all bonds. 0 if we want to update only new ones
    :param payments: 1 if we want to update payments for all bonds. 0 if we want to update only new ones
    :return:
    """

    get_all_bonds()
    get_prices()
    delete_without_prices()
    get_moex_info(moex_info) # 0 - обновляет не всё
    update_coupons()
    add_payments(payments) # 0 - обновляет не всё
    get_end_date()
    get_liquidity_month()
    change_100_amortization()
    fix_aci()
    get_yield_xirr()
