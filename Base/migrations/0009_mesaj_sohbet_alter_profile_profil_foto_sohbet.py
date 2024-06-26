# Generated by Django 5.0.3 on 2024-05-24 15:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_verilendersler_ders_seviyesi_alter_profile_bio_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mesaj',
            name='sohbet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profil_foto',
            field=models.ImageField(blank=True, null=True, upload_to='avatarlar'),
        ),
        migrations.CreateModel(
            name='Sohbet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1_sohbet', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2_sohbet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
