# Generated by Django 4.0.5 on 2023-07-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0032_emitter_report_data_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='emitter',
            name='is_report_ok',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
