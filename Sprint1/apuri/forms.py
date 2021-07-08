from django import forms
from .models import Miembro, Post, Anuncio

class Cambiarperfil(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['nombre', 'apellido_pat', 'apellido_mat', 'email', 'contraseña', 'rol', 'cel', 'institucion', 'cargo']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title','tema_post','text']

class FormAnuncios(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['autor','organ','titulo','desc','tipo','hini','hfin']