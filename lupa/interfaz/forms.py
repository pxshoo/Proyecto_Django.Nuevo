from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Card

class CartaCreacionForm(forms.ModelForm):
    titulo = forms.CharField(max_length=90, label='Título')
    descripcion = forms.CharField(max_length=180, label='Descripción')
    precio = forms.IntegerField(label='Precio')
    imagen = forms.ImageField(label='Imagen')
    url = forms.CharField(label='URL')

    class Meta:
        model = Card
        fields = ('titulo', 'descripcion', 'precio', 'imagen', 'url')