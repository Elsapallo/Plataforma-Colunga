from django.db import models
from django.utils import timezone
import pickle
    
# Create your models here.
class temas (models.Model):
    nombre_tema = models.CharField(max_length=200,verbose_name="Tema")

    def __str__(self):
        return self.nombre_tema


class Organizaciones(models.Model):
    nombre_organizacion = models.CharField(max_length=30, null=False, verbose_name="Nombre")
    pag_web = models.CharField(max_length=100, blank=True, null=True, verbose_name="Página Web")
    especial = models.CharField(max_length=100, blank=True, null=True, verbose_name="Especialidad")
    descripcion_organizacion= models.TextField(blank=True, null=True, verbose_name="descrpción")
    logo = models.ImageField(upload_to="Logos", null=True, verbose_name="Logo fundación")
    calendario = models.TextField(blank=True,null=True,verbose_name="Calendario google")

    def __str__ (self):

       return self.nombre_organizacion

opciones = [("Usuario","Usuario"),("Administrador","Administrador")]
a = 0

class Miembro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_pat = models.CharField(max_length=20, null=True, verbose_name="Apellido paterno")
    apellido_mat = models.CharField(max_length=20, null=True, verbose_name="Apellido materno")
    email = models.EmailField()
    contraseña = models.CharField(max_length=20, null=True, verbose_name="Contraseña(mín 8)")
    rol = models.CharField(max_length=40, null=False, default='Usuario', choices=opciones, verbose_name="Rol")
    cel = models.CharField(max_length=15, blank=True, null=True, verbose_name="Celular")
    institucion = models.ForeignKey(Organizaciones, null=True, on_delete=models.CASCADE, verbose_name="Institución")
    cargo = models.CharField(max_length=30, verbose_name="Cargo", blank=True, null=True)
    photo = models.ImageField(upload_to="perfil", blank=True, null=True, verbose_name="Foto de perfil")
    pin = models.IntegerField(default=000)

    def __str__(self):
        return self.email

class Post(models.Model):
    autor = models.ForeignKey(Miembro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    tema = models.ForeignKey(temas, on_delete=models.CASCADE, null=True)
    texto = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Anuncio(models.Model):
    autor = models.ForeignKey(Miembro, on_delete=models.CASCADE, verbose_name="Autor")
    organ = models.ForeignKey(Organizaciones, on_delete=models.CASCADE, verbose_name="Organización", blank=True, null=True)
    titulo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Título")
    desc = models.TextField(verbose_name="Descripción anuncio")
    tipo = models.CharField(max_length=200, verbose_name="Tipo anuncio",null=True)
    texto = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to="Anuncios",blank=True, null=True, verbose_name="Foto de Anuncio")
    hini = models.DateTimeField(blank=True, null=True, verbose_name="Inicio evento dd/mm/aa hh:mm:ss ")
    hfin = models.DateTimeField(blank=True, null=True, verbose_name="Termino evento dd/mm/aa hh:mm:ss ")

    def __str__(self):
        return self.desc

    def save(self, *args, **kwargs):
        if not self.organ:
            self.organ = None
        super(Anuncio, self).save(*args, **kwargs)
