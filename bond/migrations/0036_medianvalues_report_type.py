# Generated by Django 4.2.3 on 2023-07-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0035_medianvalues'),
    ]

    operations = [
        migrations.AddField(
            model_name='medianvalues',
            name='report_type',
            field=models.CharField(default='rsbu', max_length=4),
        ),
    ]
