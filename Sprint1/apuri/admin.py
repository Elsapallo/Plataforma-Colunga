from django.contrib import admin
from .models import Post, Miembro,Organizaciones,Anuncio, temas

class MiemborosAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido_pat", "apellido_mat", "institucion"]
    search_fields = ["nombre"]
    list_filter = ['institucion']
    exclude = ["pin"]
  #  list_per_page = 10

class OrganizacionesAdmin(admin.ModelAdmin):
    list_display = ["nombre_organizacion"]
    search_fields = ["nombre_organizacion"]
    #list_per_page = 10

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ["titulo"]
    search_fields = ["titulo"]

class TemasAdmin(admin.ModelAdmin):
    list_display = ["nombre_tema"]
    search_fields = ["nombre_tema"]

admin.site.register(Post)
admin.site.register(temas,TemasAdmin)
admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Miembro,MiemborosAdmin)
admin.site.register(Organizaciones,OrganizacionesAdmin)
# Register your models here.



