# Generated by Django 4.0.5 on 2022-10-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0011_normalvalues_industry_normal_values'),
    ]

    operations = [
        migrations.RenameField(
            model_name='normalvalues',
            old_name='absolute_liquidity',
            new_name='absolute_liquidity1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='cur_liquidity',
            new_name='cur_liquidity1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='equity_level',
            new_name='equity_level1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='fast_liquidity',
            new_name='fast_liquidity1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='interest_ratio',
            new_name='interest_ratio1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='nd_to_ebitda',
            new_name='nd_to_ebitda1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='net_margin',
            new_name='net_margin1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='operation_margin',
            new_name='operation_margin1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='roa',
            new_name='roa1',
        ),
        migrations.RenameField(
            model_name='normalvalues',
            old_name='roe',
            new_name='roe1',
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='absolute_liquidity2',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='cur_liquidity2',
            field=models.FloatField(default=75),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='ebitda_margin1',
            field=models.FloatField(default=20),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='ebitda_margin2',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='equity_level2',
            field=models.FloatField(default=8),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='fast_liquidity2',
            field=models.FloatField(default=50),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='interest_ratio2',
            field=models.FloatField(default=66),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='nd_to_ebitda2',
            field=models.FloatField(default=6),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='net_margin2',
            field=models.FloatField(default=7.5),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='operation_margin2',
            field=models.FloatField(default=9),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='roa2',
            field=models.FloatField(default=5),
        ),
        migrations.AddField(
            model_name='normalvalues',
            name='roe2',
            field=models.FloatField(default=7.5),
        ),
    ]
