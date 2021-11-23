from types import ClassMethodDescriptorType
from django import forms
from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import PasswordInput,TextInput,TextInput

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    surname = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={'class':'form-control'}))
    number = forms.CharField(label='Numero de telefono', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Meta:
    model = User
    fields = ['name','surname','number','username','password1','password2']
    help_text = {k:"" for k in fields }
    