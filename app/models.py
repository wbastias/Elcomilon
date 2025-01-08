from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# Para el Tipo

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# formulario para el producto


class Product(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre


# la opcion para el formulario de contacto
opciones_consultas = [
    [0, "Consultas"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

# Formulario para el cliente


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

# Para la Boleta

class Boleta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.IntegerField()

    def __str__(self):
        return f"Boleta {self.id} - Usuario: {self.usuario.username}"

# Para la Boleta con detalle de productos

class BoletaProduct(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, related_name='boleta_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.boleta} - {self.product.nombre}"