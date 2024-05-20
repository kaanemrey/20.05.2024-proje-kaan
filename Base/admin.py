from django.contrib import admin
from .models import DersTalepleri,Ders, Dil, VerilebilecekDersler,Mesaj,Bildirim
# Register your models here.

admin.site.register(DersTalepleri)
admin.site.register(Ders)
admin.site.register(Dil)
admin.site.register(VerilebilecekDersler)
admin.site.register(Mesaj)
admin.site.register(Bildirim)