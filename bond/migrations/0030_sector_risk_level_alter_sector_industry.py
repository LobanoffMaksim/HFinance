# Generated by Django 4.0.5 on 2023-06-12 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0029_coupon_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='risk_level',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bond.industry'),
        ),
    ]
