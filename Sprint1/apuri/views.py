from django.shortcuts import render
#from django.http import HttpResponse
#import datetime
#from django.template import Template, Context
from apuri.models import Miembro, Organizaciones
from django.core.mail import send_mail
from django.conf import settings
from random import randint
#from .forms import cambiarperfil

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
                 nombre = usuario.nombre
                 ap_pat = usuario.apellido_pat
                 ap_mat = usuario.apellido_mat
                 perfil = usuario.photo
                 mensaje = 'pase_nomas'
                 return render(request, "Inicio.html", {"query": email, "mensaje": mensaje,
                    "contraseña":contraseña, "institucion":institucion, "nombre":nombre ,"ap_pat":ap_pat, "ap_mat":ap_mat , "foto" : perfil })


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

    if request.POST["nuser"]:

        #email = request.GET["user"]
        #usuarios = Miembro.objects.filter(email__exact=email)

        #contraseña = request.GET['pass']

        email = request.POST["nuser"]
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

    if request.POST["reuser"]:
        email = request.POST["reuser"]
        usuarios = Miembro.objects.filter(email__exact=email)
        contraseña = request.POST['new_pass']
        recontraseña = request.POST['re_pass']
        pin = request.POST['pin']
        mensaje = 'Correo no registrado!'
        f = "no"

        for usuario in usuarios:
            renombre = usuario.nombre
            if contraseña != recontraseña:

                renombre = usuario.nombre
                mensaje = "Contraseñas no coinciden"
                f = "no"

            elif contraseña == "" or recontraseña == "":
                mensaje = "Por favor, ingrese al menos 8 carácteres"
                f = "no"

            elif pin != str(usuario.pin):
                f = "no"
                mensaje = "PIN incorrecto"

            else:
                mensaje = "Su contraseña fue cambiada exitosamente:)"
                f = "si"
                usuario.contraseña = recontraseña
                usuario.save()



        return render(request, "Portal.html", {"mensaje": mensaje,"f":f})

    else:
        mensaje = "Por favor, ingrese un correo"
        f = "no"
        return render(request, "Portal.html", {"mensaje": mensaje, "f":f})


def inicio(request):
    #cliente = get_object_or_404(Miembro,cel = celular)
    return render(request, 'inicio.html')

def Portal(request):
    #cliente = get_object_or_404(Miembro,cel = celular)
    return render(request, 'Portal.html')

def Organizaciones(request):
    return render(request, 'Organizaciones.html')






# Create your views here.
