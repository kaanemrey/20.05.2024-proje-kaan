# Generated by Django 5.0.3 on 2024-05-23 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_verilebilecekdersler_sehir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='konum',
        ),
        migrations.AddField(
            model_name='derstalepleri',
            name='konum',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Base.sehir'),
        ),
    ]
