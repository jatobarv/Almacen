from django.contrib.auth.models import User
from django.db import models


class Producto(models.Model):
    codigo = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True)
    imagen = models.FileField(null=True, blank=True)
    proveedor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Oferta(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    oferta = models.ForeignKey('Producto', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descuento_total = models.IntegerField()

    def __str__(self):
        return self.nombre