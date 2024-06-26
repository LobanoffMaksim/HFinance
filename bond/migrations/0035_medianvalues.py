# Generated by Django 4.2.3 on 2023-07-11 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0034_emitter_ifrs_exists'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedianValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('value', models.FloatField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bond.sector')),
            ],
        ),
    ]
