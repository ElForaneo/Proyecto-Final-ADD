from django.db import models

# Create your models here.

class Estatus(models.Model):
    id = models.AutoField(primary_key=True)
    estatus = models.CharField('Estatus',max_length=50,blank=False,null=True)

    class Meta:
        verbose_name = 'Estatu'
        verbose_name_plural = 'Estatus'
        ordering = ['id']

    def __str__(self):
        return self.estatus

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=225,blank=False,null=False,unique=True)
    producto_pedido = models.PositiveIntegerField(blank=False,null=False)
    producto_enviado = models.PositiveIntegerField(blank = False, null=True,default=0)
    producto_entregado = models.PositiveIntegerField(blank=False,null=True,default=0)
    estado = models.ForeignKey(Estatus,default=1, on_delete=models.DO_NOTHING)

    

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre