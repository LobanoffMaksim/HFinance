# Generated by Django 4.2.3 on 2023-08-16 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0037_rename_medianvalues_medianvalue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditrating',
            options={'ordering': ['id']},
        ),
    ]