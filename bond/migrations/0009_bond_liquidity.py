# Generated by Django 4.0.5 on 2022-09-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0008_emitter_credit_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='bond',
            name='liquidity',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]