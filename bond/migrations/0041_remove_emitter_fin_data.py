# Generated by Django 4.2.3 on 2024-04-04 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0040_alter_finindicator_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emitter',
            name='fin_data',
        ),
    ]
