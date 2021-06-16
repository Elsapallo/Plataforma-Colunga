from django.contrib import admin
from .models import Post, Miembro,Organizaciones

class MiemborosAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido_pat","apellido_mat","institucion"]
    search_fields = ["nombre"]
    exclude = ["pin"]
  #  list_per_page = 10

class OrganizacionesAdmin(admin.ModelAdmin):
    list_display = ["nombre_organizacion"]
    search_fields = ["nombre_organizacion"]
    #list_per_page = 10

admin.site.register(Post)
admin.site.register(Miembro,MiemborosAdmin)
admin.site.register(Organizaciones,OrganizacionesAdmin)
# Register your models here.



