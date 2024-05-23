from django.urls import path 
from . import views

urlpatterns = [
  path('',views.MainPage, name='Home'),
  path('login/', views.login_page, name='login'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_page, name='register'),
  path('biz_kimiz/', views.biz_kimiz, name='biz_kimiz'),
  path('derstalepleri/', views.derstalepleri,name='DersTalepleri'),
  path('OzelDers/',views.OzelDers,name='OzelDers' ),
  path('talepolustur/',views.TalepOlustur,name='TalepOlustur' ),
  path('talep_detay/<str:pk>/', views.talep_detay, name='TalepDetay'),
  path('talep_sil/<str:pk>/', views.talep_sil, name='TalepSil'),
  path('talep_duzenle/<str:pk>/', views.talep_duzenle, name='TalepDuzenle'),
  path('matematik/',views.Matematik, name='matematik'),
  path('python/',views. Python, name='python'),
  path('fizik/',views.Fizik, name='fizik'),
  path('gitar/',views.Gitar, name='gitar'),
  path('profil/<str:pk>/',views.Profil, name='profil'),
  path('mesaj/',views.Mesaj, name='mesaj'),
  path('talebi_kabul_et/<str:pk>',views.talep_kabul, name='TalepKabul'),
  path('verdigim_dersler/<str:pk>/',views.verdigim_dersler,name='VerdigimDersler'),
  path('ders_ekle/<str:pk>/',views.ders_ekle,name='DersEkle'),  
  path('ders_sik/<str:pk>/',views.ders_sil,name='DersSil'),
  path('ders_duzenle/<str:pk>/',views.ders_duzenle,name='DersDuzenle'),
  path('avatar_guncelle/<str:pk>/',views.avatar_guncelle,name='AvatarGuncelle'),
]


