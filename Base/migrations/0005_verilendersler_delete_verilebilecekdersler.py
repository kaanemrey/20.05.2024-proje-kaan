# Generated by Django 5.0.3 on 2024-05-23 20:03

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_remove_profile_konum_derstalepleri_konum'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VerilenDersler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saatlik_ucret', models.IntegerField(validators=[django.core.validators.MaxValueValidator(0)])),
                ('ders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.ders')),
                ('ders_dili', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.dil')),
                ('egitmen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sehir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Base.sehir')),
            ],
        ),
        migrations.DeleteModel(
            name='VerilebilecekDersler',
        ),
    ]
