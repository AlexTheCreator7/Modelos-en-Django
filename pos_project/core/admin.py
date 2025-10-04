from django.contrib import admin
from .models import GrupoArticulo, LineaArticulo, Articulo, ListaPrecio

admin.site.register(GrupoArticulo)
admin.site.register(LineaArticulo)
admin.site.register(Articulo)
admin.site.register(ListaPrecio)