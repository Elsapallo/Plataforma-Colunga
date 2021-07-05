from django.db import models
from django.utils import timezone
import pickle
    
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Organizaciones(models.Model):
    nombre_organizacion= models.CharField(max_length=30, null=False)
    pag_web = models.CharField(max_length=100, null=True)
    descripcion_organizacion= models.TextField(null=True)
    logo = models.ImageField(upload_to="Logos", null=True, verbose_name="Logo institución")
    #miembros = models.ForeignKey(Miembro, null=True, blank=True, on_delete=models.CASCADE)
    def __str__ (self):

       return self.nombre_organizacion

opciones = [("Usuario","Usuario"),("Administrador","Administrador")]
a = 0
#org = Organizaciones.objects.all()

#org = Organizaciones.objects.values_list('id', 'nombre_organizacion')

#for i in org:
    #opciones.append(list(i))###


class Miembro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=20, null=True, verbose_name="Apellido paterno")
    apellido_mat = models.CharField(max_length=20, null=True, verbose_name="Apellido materno")
    email = models.EmailField()
    contraseña = models.CharField(max_length=20, null=True)
    rol = models.CharField(max_length=40, null=False, default='Usuario', choices=opciones, verbose_name="Rol")
    cel = models.CharField(max_length=15, verbose_name="Celular")
    institucion = models.ForeignKey(Organizaciones, null=True, on_delete=models.CASCADE, verbose_name="Institución")
    cargo = models.CharField(max_length=30, verbose_name="Cargo", null=True)
    photo = models.ImageField(upload_to="perfil", null=True, verbose_name="Foto de perfil")
    pin = models.IntegerField(default=000)

    def __str__(self):

        return self.nombre

class Anuncio(models.Model):
    autor = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    texto = models.TextField()
    foto = models.ImageField(upload_to="Anuncios", null=True, verbose_name="Foto de Anuncio")
