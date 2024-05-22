from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE, SET_NULL, SET_DEFAULT

class Dil(models.Model):
  dil = models.CharField(max_length=50)
  def __str__(self):
    return self.dil
  

class Ders(models.Model):
  ders = models.CharField(max_length=50)

  def __str__(self) :
    return self.ders


class DersTalepleri(models.Model):
  seviye = [
    ('ilkokul', 'İlkokul'),
    ('ortaokul', 'Ortaokul'),
    ('lise', 'Lise'),
    ('universite', 'Üniversite'),
    ('yukseklisans','Yüksek Lisans'),
  ]
  kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
  isim = models.CharField(max_length=50)
  ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
  talep_notu= models.TextField(max_length=200,null=True,blank=True)
  talep_durumu = models.BooleanField(default=False)
  min_butce = models.IntegerField(validators=[MinValueValidator(0)])
  max_butce = models.IntegerField(validators=[MaxValueValidator(10000)])
  ogrenci_seviyesi = models.CharField(max_length=50,choices=seviye)
  olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.isim
  
class VerilebilecekDersler(models.Model):
  ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
  saatlik_ucret = models.IntegerField()
  egitmen = models.ForeignKey(User, on_delete=models.CASCADE)
  ders_dili = models.ForeignKey(Dil,on_delete=models.CASCADE)
  
  def __str__(self):
    return  f'{self.egitmen}   Dersin Dili:{self.ders_dili}   Ders:{self.ders}   Ücret:{self.saatlik_ucret}'
  

class Mesaj(models.Model):
  gönderen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gönderilen_mesajlar')
  alici = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alınan_mesajlar')
  tarih = models.DateTimeField(auto_now_add=True)
  içerik = models.TextField(max_length=200)

  def __str__(self):
    return f'{self.gönderen} --> {self.alici}: {self.içerik[0:50]}'
  
class Bildirim(models.Model):
  alici = models.ForeignKey(User, on_delete=CASCADE)
  icerik = models.TextField(max_length=200)
  tarih = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.icerik[0:50]}--{self.alici}"


class Profile(models.Model):
  secenek1 = [
    ('erkek','Erkek'),
    ('kadin','Kadın'),
  ]
  secenek2 = [
    ('egitmen','Eğitmen'),
    ('ogrenci','Öğrenci'),
  ]
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  kullanici_tipi = models.CharField(max_length=50,null=False, choices=secenek2)
  bio = models.TextField(max_length=200, null=True,blank=True, default='')
  konum = models.CharField(max_length=50,null=True,blank=True, default='')
  # profil_foto = models.ImageField(upload_to='profil_fotolar/',null=True,blank=True,)
  dogum_tarihi = models.DateField(null=True, blank=True, default='')
  tel_no = models.CharField(max_length=20, null=True, blank=True, default='')
  cinsiyet = models.CharField(max_length=50,choices=secenek1)
  
  def __str__(self):
    return str(self.user)
  

class OgrenciProfile(models.Model):
  choices = [
    ('ilkokul', 'İlkokul'),
    ('ortaokul', 'Ortaokul'),
    ('lise', 'Lise'),
    ('universite', 'Üniversite'),
    ('yukseklisans','Yüksek Lisans'),
  ]
  profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
  seviye = models.CharField(max_length=50, choices=choices)
  
  def __str__(self):
    return f'{self.profile.user.username} - Öğrenci'


class EgitmenProfile(models.Model):
  profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.profile.user.username} - Eğitmen'
  
  