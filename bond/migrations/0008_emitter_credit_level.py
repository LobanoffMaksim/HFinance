# Generated by Django 4.0.5 on 2022-09-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0007_alter_emitter_options_alter_coupon_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emitter',
            name='credit_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
