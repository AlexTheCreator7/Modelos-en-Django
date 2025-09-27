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
        verbose_name = 'Grupo de Artículo'
        verbose_name_plural = 'Grupos de Artículos'

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
        verbose_name = 'Línea de Artículo'
        verbose_name_plural = 'Líneas de Artículos'