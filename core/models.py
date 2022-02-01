from django.db import models

# Create your models here.
class Pedidos(models.Model):

    pedido = models.IntegerField("Pedido", max_length=15)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    expireAt = models.DateField("Data de expiração")
    status = models.CharField('Status', max_length=100, default="Pendente")
    qrcode = models.CharField('QRcode', max_length=300)