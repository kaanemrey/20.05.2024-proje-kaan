# Generated by Django 5.0.3 on 2024-05-24 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0009_mesaj_sohbet_alter_profile_profil_foto_sohbet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesaj',
            name='sohbet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='Base.sohbet'),
        ),
    ]
