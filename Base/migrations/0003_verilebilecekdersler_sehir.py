# Generated by Django 5.0.3 on 2024-05-23 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_profile_konum'),
    ]

    operations = [
        migrations.AddField(
            model_name='verilebilecekdersler',
            name='sehir',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Base.sehir'),
        ),
    ]
