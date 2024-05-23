from django.contrib import admin
from .models import DersTalepleri, Ders, Dil, VerilenDersler, Mesaj, Bildirim, Profile, OgrenciProfile, EgitmenProfile, Sehir
# Register your models here.

admin.site.register(Profile)
admin.site.register(DersTalepleri)
admin.site.register(Ders)
admin.site.register(Dil)
admin.site.register(VerilenDersler)
admin.site.register(Mesaj)
admin.site.register(Bildirim)
admin.site.register(OgrenciProfile)
admin.site.register(EgitmenProfile)
admin.site.register(Sehir)