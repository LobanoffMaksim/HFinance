# Generated by Django 4.0.5 on 2023-05-02 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0023_alter_finindicator_options_emitter_need_add_fin_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('value', models.CharField(max_length=10)),
                ('emitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bond.emitter')),
            ],
        ),
    ]