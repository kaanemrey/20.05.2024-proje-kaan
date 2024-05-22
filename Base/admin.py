from django.contrib import admin
from .models import DersTalepleri, Ders, Dil, VerilebilecekDersler, Mesaj, Bildirim, Profile, OgrenciProfile, EgitmenProfile
# Register your models here.

admin.site.register(Profile)
admin.site.register(DersTalepleri)
admin.site.register(Ders)
admin.site.register(Dil)
admin.site.register(VerilebilecekDersler)
admin.site.register(Mesaj)
admin.site.register(Bildirim)
admin.site.register(OgrenciProfile)
admin.site.register(EgitmenProfile)