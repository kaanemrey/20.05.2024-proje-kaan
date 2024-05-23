
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile,User
'''
@receiver(post_save, sender=Profile)
def update_ders_sehir(sender, instance, **kwargs):
    user = instance.user
    dersler = VerilebilecekDersler.objects.filter(egitmen=user)
    for ders in dersler:
        ders.sehir = instance.konum
        ders.save()
        '''