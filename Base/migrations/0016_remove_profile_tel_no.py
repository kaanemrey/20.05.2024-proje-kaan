# Generated by Django 5.0.3 on 2024-05-26 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0015_alter_derstalepleri_dil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tel_no',
        ),
    ]