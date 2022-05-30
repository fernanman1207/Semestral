from django.db import models

class Fruta(models.Model):
    nombrefruta = models.CharField(primary_key=True, max_length=30, verbose_name='Nombre de la fruta',blank=False, null=False)
    cantidadfruta = models.IntegerField(max_length=4, verbose_name='cantidad de fruta')
    preciofruta = models.IntegerField(verbose_name='precio fruta')
    fotofruta = models.ImageField(upload_to="foto_fruta", null= True)

    def __str__(self):
        return self.nombrefruta


class cliente(models.Model):
    nombrecliente = models.CharField(max_length=30, verbose_name='Nombre del cliente')
    apellidocliente = models.CharField(max_length=50,verbose_name='apellido del cliente')
    rutcliente = models.IntegerField(primary_key=True, verbose_name='rut cliente (use numeros)')
    correocliente = models.IntegerField(max_length=30,verbose_name='introduzca su correo')
    clavecliente = models.CharField(max_length=20, verbose_name='introduzca su clave')

    def __str__(self):
        return self.nombrecliente
