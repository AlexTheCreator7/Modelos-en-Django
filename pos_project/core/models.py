import uuid
from django.db import models
from pos_project.choices import EstadoEntidades

class GrupoArticulo(models.Model):
    grupo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_grupo = models.CharField(max_length=10, null=False)
    nombre_grupo = models.CharField(max_length=100, null=False)
    estado = models.IntegerField(choices=EstadoEntidades.choices, default=EstadoEntidades.ACTIVO)

    def __str__(self):
        return self.nombre_grupo

    class Meta:
        db_table = 'grupos_articulos'


class LineaArticulo(models.Model):
    linea_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_linea = models.CharField(max_length=10, null=False)
    nombre_linea = models.CharField(max_length=100, null=False)
    grupo = models.ForeignKey(GrupoArticulo, on_delete=models.RESTRICT, related_name='grupos_lineas')
    estado = models.IntegerField(choices=EstadoEntidades.choices, default=EstadoEntidades.ACTIVO)

    def __str__(self):
        return self.nombre_linea

    class Meta:
        db_table = 'lineas_articulos'


class Articulo(models.Model):
    articulo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_articulo = models.CharField(max_length=20, unique=True)
    codigo_barras = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=200)
    presentacion = models.CharField(max_length=100, null=True, blank=True)
    grupo = models.ForeignKey(GrupoArticulo, on_delete=models.RESTRICT)
    linea = models.ForeignKey(LineaArticulo, on_delete=models.RESTRICT)
    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.IntegerField(choices=EstadoEntidades.choices, default=EstadoEntidades.ACTIVO)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'articulos'


class ListaPrecio(models.Model):
    lista_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE, related_name='listaprecio')
    precio_1 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_4 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Precios de {self.articulo.descripcion}"

    class Meta:
        db_table = 'lista_precios'