# Generated by Django 4.0.5 on 2022-07-13 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0004_bond_facevalue_bond_price_bond_start_facevalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emitter',
            name='akra',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='ceo',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='fin_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='fin_file',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bond.emitterfinfile'),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='fitch',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='is_system_important',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='moex_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='moodys',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='netdebt_to_assets',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='netdebt_to_ebitda',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='netdebt_to_equity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='ra_expert',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='revenue',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bond.sector'),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='sp',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='title',
            field=models.CharField(max_length=52, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='website1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emitter',
            name='website2',
            field=models.URLField(blank=True, null=True),
        ),
    ]