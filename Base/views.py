from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .formlar import RegisterForm , DersTalepleriForm, ProfileForm, ProfileEditForm, UserEditForm, DersEkleForm, AvatarForm, MessageForm
from .models import DersTalepleri, EgitmenProfile, OgrenciProfile, Profile, VerilenDersler, Mesaj, Sohbet


def login_page(request):
  sayfa = 'login'
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'Böyle bi kullanıcı ismi bulunmuyor')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect('Home')
    else:
      messages.error(request, 'Yanlış Şifre')
  context = {'sayfa': sayfa}
  return render(request, 'Log-Sign.html',context)


def logout_user(request):
  logout(request)
  return redirect('Home')


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save() 
            if profile.kullanici_tipi == 'egitmen':
                d = {'profile':profile}
                egitmen = EgitmenProfile.objects.create(**d) 
                egitmen.save()
            elif profile.kullanici_tipi == 'ogrenci':
                d = {'profile':profile}
                ogrenci = OgrenciProfile.objects.create(**d)
                ogrenci.save()          
            login(request, user)
            return redirect('Home')  
    else:
        form = RegisterForm()
        profile_form = ProfileForm()
    context = {
       'form': form , 
       'profile_form': profile_form, 
       }
    return render(request, 'Log-Sign.html', context)


def MainPage(request):
  return render(request,'MainPage.html')


def OzelDers(request):
   dersler = VerilenDersler.objects.all()
   context = {'dersler' : dersler}
   return render(request,'OzelDers.html',context)

def hoca_detay(request,pk):
   ders = VerilenDersler.objects.get(id=pk)
   user = ders.egitmen
   profile = Profile.objects.get(user=user)
   if profile.bio:
      has_bio = True
   else:
      has_bio = False
   context = {'ders' : ders, 'user' : user, 'has_bio' : has_bio}
   return render(request,'HocaDetay.html',context)
   

def biz_kimiz(request):
   return render(request,'hakkımızda.html')  


def derstalepleri(request):
   derstalepleri = DersTalepleri.objects.all()
   context = {'derstalepleri': derstalepleri}
   return render(request, 'DersTalepleri.html',context)


def TalepOlustur(request):
    user = request.user
    if request.method == 'POST':
        min=request.POST.get('min_butce')
        max=request.POST.get('max_butce')
        min = int(min)
        max = int(max)
        if max >= min:
           form = DersTalepleriForm(request.POST)
           if form.is_valid():
             ders_talebi = form.save(commit=False)
             ders_talebi.kullanici = user
             ders_talebi.save()
             return redirect('DersTalepleri')
        else:
            messages.error(request,'Minimum bütçe aralığı maksimum bütçe aralığından büyük olamaz')
            form = DersTalepleriForm()
    else:
        form = DersTalepleriForm()
    return render(request, 'TalepOluştur.html', {'form': form})


def talep_detay(request, pk):
    ders_talebi = DersTalepleri.objects.get(id=pk)
    return render(request, 'TalepDetay.html', {'ders_talebi': ders_talebi})


def talep_sil(request, pk):
   ders_talebi = DersTalepleri.objects.get(id=pk)
   ders_talebi.delete()
   return redirect('DersTalepleri')


def talep_duzenle(request, pk):
   ders_talebi = DersTalepleri.objects.get(id=pk)
   if request.method == 'POST':
        min=request.POST.get('min_butce')
        max=request.POST.get('max_butce')
        if max >= min:
           form = DersTalepleriForm(request.POST, instance=ders_talebi)
           if form.is_valid():
             form.save()
             return redirect('DersTalepleri')
        else:
            messages.error(request,'Minimum bütçe aralığı maksimum bütçe aralığından büyük olamaz')
            form = DersTalepleriForm()
   else:
      form = DersTalepleriForm(instance=ders_talebi)
    
   return render(request, 'TalepOluştur.html', {'form': form})


def talep_kabul(request,pk):
   ders_talebi = DersTalepleri.objects.get(id=pk)
   ders_talebi.talep_durumu = True
   ders_talebi.save()
   return redirect('DersTalepleri')


def Matematik(request):
    return render(request, 'matematik.html')


def Python(request):
    return render(request, 'python.html')


def Fizik(request):
    return render(request, 'fizik.html')


def Gitar(request):
    return render(request, 'gitar.html')


def Profil(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    context = {}
    if profile.profil_foto:
        has_profile_photo = True
    else:
        has_profile_photo = False

    if request.method == 'POST':  
        userform = UserEditForm(request.POST, instance=user)
        profileform = ProfileEditForm(request.POST, instance=profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('profil',pk=request.user.pk)
    else:
        profileform = ProfileEditForm(instance=profile)
        userform = UserEditForm(instance=user)
    
    context = {'profileform': profileform, 'userform': userform, 'profile': profile,'has_profile_photo': has_profile_photo}
    return render(request, 'profil.html', context)


def verdigim_dersler(request,pk):
   user = User.objects.get(id=pk)
   dersler = VerilenDersler.objects.filter(egitmen=user) 
   return render(request,'VerdigimDersler.html',{'dersler':dersler})

def ders_ekle(request,pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
       dersform = DersEkleForm(request.POST)
       if dersform.is_valid():
          ders = dersform.save(commit=False)
          ders.egitmen = user
          ders.save()    
          return redirect('VerdigimDersler', pk=user.id)   
    else:
       dersform = DersEkleForm()
    return render(request,'DersEkle.html',{'dersform':dersform})

def ders_sil(request,pk):
   ders = VerilenDersler.objects.get(id=pk)
   ders.delete()
   return redirect('VerdigimDersler', pk=request.user.id)

def ders_duzenle(request,pk):
   ders_data = VerilenDersler.objects.get(id=pk)
   if request.method == 'POST':
      dersform = DersEkleForm(request.POST,instance=ders_data)
      if dersform.is_valid():
         dersform.save()
         return redirect('VerdigimDersler', pk= request.user.id)
   else:
      dersform = DersEkleForm(instance=ders_data)
   return render(request,'DersEkle.html',{'dersform':dersform})


def avatar_guncelle(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profil', pk=pk)  
    else:
        form = AvatarForm(instance=profile)
    return render(request, 'AvatarGuncelle.html', {'form': form})
   



def mesaj(request):
   user = request.user 
   sohbetler = Sohbet.objects.filter(user1=user) | Sohbet.objects.filter(user2=user)
   context = {'sohbetler': sohbetler}
   return render(request, 'mesaj.html',context)


def sohbet_detay(request,pk):
   user = request.user 
   sohbetler = Sohbet.objects.filter(user1=user) | Sohbet.objects.filter(user2=user)
   secili_sohbet = Sohbet.objects.get(id=pk)
   mesajlar = Mesaj.objects.filter(sohbet=secili_sohbet)
   if request.method == 'POST':
      mesajform = MessageForm(request.POST)
      yeni_mesaj = mesajform.save(commit=False)
      yeni_mesaj.gönderen = user
      yeni_mesaj.sohbet = secili_sohbet
      yeni_mesaj.save()
      mesajlar = Mesaj.objects.filter(sohbet=secili_sohbet)
   else:
      mesajform = MessageForm()
   context = {'sohbetler' : sohbetler, 'secili_sohbet' : secili_sohbet, 'mesajlar' : mesajlar, 'mesajform' : mesajform}
   return render(request,'mesaj.html',context)


def iletisime_gec1(request, pk):
    ders_talebi = DersTalepleri.objects.get(id=pk)
    alici = ders_talebi.kullanici
    user = request.user
    sohbetler = Sohbet.objects.filter(Q(user1=user) | Q(user2=user))
    try:
        secili_sohbet = Sohbet.objects.get(
        Q(user1=user, user2=alici) | Q(user1=alici, user2=user)
    )
    except Sohbet.DoesNotExist:
        secili_sohbet = Sohbet.objects.create(user1=user, user2=alici)
    mesajlar = Mesaj.objects.filter(sohbet=secili_sohbet)
    if request.method == 'POST':
        mesajform = MessageForm(request.POST)
        if mesajform.is_valid():
            yeni_mesaj = mesajform.save(commit=False)
            yeni_mesaj.gönderen = user
            yeni_mesaj.sohbet = secili_sohbet
            yeni_mesaj.save()
            return redirect('IletisimeGec',pk=ders_talebi.id)
    else:
        mesajform = MessageForm()
    context = {
        'sohbetler': sohbetler,
        'secili_sohbet': secili_sohbet,
        'mesajlar': mesajlar,
        'mesajform': mesajform
    }
    return render(request, 'mesaj.html', context)
    

def iletisime_gec2(request, pk):
    ders = VerilenDersler.objects.get(id=pk)
    alici = ders.egitmen
    user = request.user
    sohbetler = Sohbet.objects.filter(Q(user1=user) | Q(user2=user))
    try:
        secili_sohbet = Sohbet.objects.get(
        Q(user1=user, user2=alici) | Q(user1=alici, user2=user)
    )
    except Sohbet.DoesNotExist:
        secili_sohbet = Sohbet.objects.create(user1=user, user2=alici)
    mesajlar = Mesaj.objects.filter(sohbet=secili_sohbet)
    if request.method == 'POST':
        mesajform = MessageForm(request.POST)
        if mesajform.is_valid():
            yeni_mesaj = mesajform.save(commit=False)
            yeni_mesaj.gönderen = user
            yeni_mesaj.sohbet = secili_sohbet
            yeni_mesaj.save()
            return redirect('IletisimeGec2',pk=ders.id)
    else:
        mesajform = MessageForm()
    context = {
        'sohbetler': sohbetler,
        'secili_sohbet': secili_sohbet,
        'mesajlar': mesajlar,
        'mesajform': mesajform
    }
    return render(request, 'mesaj.html', context)


