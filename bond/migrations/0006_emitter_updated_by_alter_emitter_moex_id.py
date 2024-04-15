# Generated by Django 4.0.5 on 2022-07-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0005_alter_emitter_akra_alter_emitter_ceo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emitter',
            name='updated_by',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='moex_id',
            field=models.IntegerField(unique=True),
        ),
    ]