# Generated by Django 5.0.3 on 2024-05-23 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0005_verilendersler_delete_verilebilecekdersler'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profil_foto',
            field=models.ImageField(blank=True, null=True, upload_to='avatarlar/'),
        ),
        migrations.AlterField(
            model_name='verilendersler',
            name='saatlik_ucret',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]