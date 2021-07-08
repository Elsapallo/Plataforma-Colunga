from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('Login/', views.Login ),
    path('Refoto/', views.Refoto, name='Refoto'),
    path('Recuperacion/', views.Recuperacion),
    path('Re_contraseña/',views.Re_contraseña),
    path('', views.Portal, name='Portal'),
    path('editar/', views.foro.crear_foro, name='editar'),
    path('Foro/', views.foro.mostrar_foros, name='foro'),
    path('crear_anuncio/', views.anun.crear_anuncios, name='anuncios'),
    path('Cambiarperfil/', views.perfil.Cambiarperfil, name='nusuario'),
    path('Login/crear_anuncio.html/', views.anun.crear_anuncios, name='anuncios'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)