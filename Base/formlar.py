from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DersTalepleri


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Kullanıcı İsmi', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Şifreyi Onaylayın', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class DersTalepleriForm(forms.ModelForm):
    class Meta:
        model = DersTalepleri
        fields = ['kullanici','isim' , 'ders' , 'talep_notu' , 'min_butce' , 'max_butce' , 'ogrenci_seviyesi']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-input'})

        

