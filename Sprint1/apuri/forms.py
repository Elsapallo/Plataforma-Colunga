from django import forms
from .models import Miembro, Post, Anuncio

class Cambiarperfil(forms.ModelForm):

    class Meta:
        model = Miembro
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class FormAnuncios(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = '__all__'