from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import DersTalepleri


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Kullanıcı İsmi', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Şifre', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Şifreyi Onaylayın', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        try:
            validate_password(password1, self.instance)
        except ValidationError as error:
            raise ValidationError(_("Bu şifre çok kısa. En az 8 karakter içermelidir.")) from error
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Girilen şifreler eşleşmiyor."))
        return password2
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DersTalepleriForm(forms.ModelForm):
    class Meta:
        model = DersTalepleri
        fields = ['kullanici', 'isim', 'ders', 'talep_notu', 'min_butce', 'max_butce', 'ogrenci_seviyesi']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-input'})
