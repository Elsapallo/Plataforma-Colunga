from django.shortcuts import render
#from django.http import HttpResponse
#import datetime
#from django.template import Template, Context
from apuri.models import Miembro, Organizaciones, Anuncio, Post, temas
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from .forms import PostForm,FormAnuncios, Cambiarperfil

def post_list(request):
    return render(request, 'Portal.html', {})


def Login(request):

    if request.POST["user"]:
        #mensaje_usu = 'Usuario: %r <br> ' %request.GET["user"]
        email = request.POST["user"]
        usuarios = Miembro.objects.filter(email__exact=email)

        contraseña = request.POST['pass']

        mensaje = 'Correo incorrecto'
        f = "no"

        for usuario in usuarios:

             if usuario.contraseña == contraseña:

                 institucion = usuario.institucion
                 google = institucion.calendario
                 miembros = Miembro.objects.all()
                 org = Organizaciones.objects.all()
                 anunciont = Anuncio.objects.all()
                 anuncios = []
                 a = 0
                 for i in reversed(anunciont):
                     if a < 3:
                         if i.organ == institucion or i.organ==None:
                            anuncios.append(i)
                            a += 1
                 print(anuncios)
                 nombre = usuario.nombre
                 ap_pat = usuario.apellido_pat
                 ap_mat = usuario.apellido_mat
                 rol = usuario.rol
                 perfil = usuario.photo
                 mensaje = 'pase_nomas'
                 if a == 0:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, 'nanuncios': a, "calendario":google,
                    "contraseña": contraseña, "institucion": institucion, "nombre": nombre, "ap_pat": ap_pat, "ap_mat":ap_mat, "foto" : perfil, "org": org, "rol": rol, "miembros": miembros})
                 elif a == 1:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, "anuncio1": anuncios[0],"calendario":google,
                                                            "anuncio2": anuncios[1], "anuncio3": anuncios[2],
                                                            "contraseña": contraseña, "institucion": institucion,
                                                            "nombre": nombre, "ap_pat": ap_pat, "ap_mat": ap_mat,
                                                            "foto": perfil, "org": org, "rol": rol,
                                                            "miembros": miembros})
                 elif a == 2:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, "anuncio1": anuncios[0],"calendario":google,
                                                            "anuncio2": anuncios[1], 'nanuncios': a,
                                                            "contraseña": contraseña, "institucion": institucion,
                                                            "nombre": nombre, "ap_pat": ap_pat, "ap_mat": ap_mat,
                                                            "foto": perfil, "org": org, "rol": rol,
                                                            "miembros": miembros})
                 else:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, "anuncio1": anuncios[0],"calendario":google,
                                                            "anuncio2": anuncios[1], "anuncio3": anuncios[2], 'nanuncios': a,
                                                            "contraseña": contraseña, "institucion": institucion,
                                                            "nombre": nombre, "ap_pat": ap_pat, "ap_mat": ap_mat,
                                                            "foto": perfil, "org": org, "rol": rol,
                                                            "miembros": miembros})
             elif usuario.contraseña != contraseña:
                 nombre = usuario.nombre
                 mensaje = 'Contraseña incorrecta'
                 f = "no"
                 return render(request, "Portal.html", {"query": email, "mensaje": mensaje, "nombre":nombre,"f":f})

             else :
                 f = "no"
                 nombre = usuario.nombre
                 mensaje = "no_flaco"
                 return render(request, "Portal.html", {"query": email, "mensaje": mensaje, "nombre": nombre,"f":f})


    else:
        mensaje = ''
        f = "ni"

    return render(request, "Portal.html", { "mensaje": mensaje,"f":f})

def Recuperacion(request):

    if request.GET["nuser"]:
        email = request.GET["nuser"]
        usuarios = Miembro.objects.filter(email__exact=email)
        mensaje = 'El correo que ingresó no está registrado '
        f = "no"
        for usuario in usuarios:
                f = "si"
                mensaje = "el PIN ha sido enviado a su correo correctamente"
                renombre = usuario.nombre
                uwu = randint(10000, 99999)
                usuario.pin = uwu
                usuario.save()
                subject = "Recuperación contraseña Colunga"
                message = "Estimad@ "+ str(renombre) + " su Pin para cambiar su contraseña es: "+ str(uwu)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                return render(request, "Portal.html", {"query": email, "mensaje": mensaje, "renombre": renombre, "f":f})

    else:
        mensaje = ''
        f = "ni"

    return render(request, "Portal.html", { "mensaje": mensaje, "f":f})


def Re_contraseña(request):

    if request.GET["reuser"]:
        email = request.GET["reuser"]
        usuarios = Miembro.objects.filter(email__exact=email)
        contraseña = request.GET['new_pass']
        recontraseña = request.GET['re_pass']
        pin = request.GET['pin']
        mensaje = 'Correo no registrado!'
        f = "no"
        for usuario in usuarios:
            if contraseña != recontraseña:
                mensaje = "Contraseñas no coinciden"
                f = "no"

            elif contraseña == "" or recontraseña == "":
                mensaje = "Por favor, ingrese al menos 8 carácteres"
                f = "no"

            elif pin != str(usuario.pin):
                f = "no"
                mensaje = "PIN incorrecto"

            else:
                mensaje = "Su contraseña fue cambiada exitosamente :)"
                f = "si"
                usuario.contraseña = recontraseña
                usuario.save()

        return render(request, "Portal.html", {"mensaje": mensaje,"f":f})

    else:
        mensaje = "Por favor, ingrese un correo"
        f = "no"
        return render(request, "Portal.html", {"mensaje": mensaje, "f":f})

def Refoto(request):
    if request.POST['user']:
        #mensaje_usu = 'Usuario: %r <br> ' %request.GET["user"]
        email = request.POST["user"]
        usuarios = Miembro.objects.filter(email__exact=email)

        contraseña = request.POST['pass']

        mensaje = 'Correo incorrecto'
        f = "no"

        for usuario in usuarios:

             if usuario.contraseña == contraseña:

                 institucion = usuario.institucion
                 google = institucion.calendario
                 miembros = Miembro.objects.all()
                 org = Organizaciones.objects.all()
                 anunciont = Anuncio.objects.all()
                 if request.FILES["poto"]:
                    foto = request.FILES["poto"]
                    unu = "sifoto"
                    usuario.photo = foto
                    usuario.save()
                 else:
                    unu = "nofoto"
                 anuncios = []
                 a = 0
                 for i in reversed(anunciont):
                     if a < 3:
                         if i.organ == institucion or i.organ==None:
                            anuncios.append(i)
                            a += 1
                 print(anuncios)
                 nombre = usuario.nombre

                 ap_pat = usuario.apellido_pat
                 ap_mat = usuario.apellido_mat
                 rol = usuario.rol
                 perfil = usuario.photo
                 mensaje = 'pase_nomas'
                 if a == 0:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, 'nanuncios': a, "calendario":google,"unu":unu,
                    "contraseña": contraseña, "institucion": institucion, "nombre": nombre, "ap_pat": ap_pat, "ap_mat":ap_mat, "foto" : perfil, "org": org, "rol": rol, "miembros": miembros})
                 elif a == 1:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, "anuncio1": anuncios[0],"calendario":google,
                                                            "anuncio2": anuncios[1], "anuncio3": anuncios[2],"unu":unu,
                                                            "contraseña": contraseña, "institucion": institucion,
                                                            "nombre": nombre, "ap_pat": ap_pat, "ap_mat": ap_mat,
                                                            "foto": perfil, "org": org, "rol": rol,
                                                            "miembros": miembros})
                 elif a == 2:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, "anuncio1": anuncios[0],"calendario":google,
                                                            "anuncio2": anuncios[1], 'nanuncios': a,"unu":unu,
                                                            "contraseña": contraseña, "institucion": institucion,
                                                            "nombre": nombre, "ap_pat": ap_pat, "ap_mat": ap_mat,
                                                            "foto": perfil, "org": org, "rol": rol,
                                                            "miembros": miembros})
                 else:
                     return render(request, "Inicio.html", {"query": email, "mensaje": mensaje, "anuncio1": anuncios[0],"calendario":google,
                                                            "anuncio2": anuncios[1], "anuncio3": anuncios[2], 'nanuncios': a,
                                                            "contraseña": contraseña, "institucion": institucion,"unu":unu,
                                                            "nombre": nombre, "ap_pat": ap_pat, "ap_mat": ap_mat,
                                                            "foto": perfil, "org": org, "rol": rol,
                                                            "miembros": miembros})
             elif usuario.contraseña != contraseña:
                 nombre = usuario.nombre
                 mensaje = 'Contraseña incorrecta'
                 f = "no"
                 return render(request, "Portal.html", {"query": email, "mensaje": mensaje, "nombre":nombre,"f":f})

             else :
                 f = "no"
                 nombre = usuario.nombre
                 mensaje = "no_flaco"
                 return render(request, "Portal.html", {"query": email, "mensaje": mensaje, "nombre": nombre,"f":f})


    else:
        mensaje = ''
        f = "ni"

    return render(request, "Portal.html", { "mensaje": mensaje,"f":f})




def Portal(request):
    return render(request, 'Portal.html')


class anun():

    def crear_anuncios(request):
        if request.method == "POST":
            form = FormAnuncios(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return render(request, 'crear_anuncio.html', {'form': form})
        else:
            form = FormAnuncios()
        return render(request, 'crear_anuncio.html', {'form': form})


class foro():

    def crear_foro(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return render(request, 'crearforo.html', {'form': form})
        else:
            form = PostForm()
        return render(request, 'crearforo.html', {'form': form})

    def mostrar_foros(request):
        form = Post.objects.all()
        farm = temas.objects.all()
        return render(request, 'Foro.html', {'form': form, 'farm': farm })
# Create your views here.
