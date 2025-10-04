from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.articulos_list, name='articulos_list'),
    path('articulos/nuevo/', views.articulo_create, name='articulo_create'),
    path('articulos/<uuid:articulo_id>/', views.articulo_detail, name='articulo_detail'),
    path('articulos/<uuid:articulo_id>/editar/', views.articulo_edit, name='articulo_edit'),
]