from django.db import models

class Produto(models.Model):
    loja = models.CharField(max_length=100, null=True, blank=True)
    endereco1 = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)

    uniformes = models.IntegerField(null=True, blank=True)
    vol_unif = models.FloatField(null=True, blank=True)

    cam_bone = models.IntegerField(null=True, blank=True)
    vol_cb = models.FloatField(null=True, blank=True)

    vol = models.FloatField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)

    nota = models.CharField(max_length=50, null=True, blank=True)
    emite_nf = models.CharField(max_length=10, null=True, blank=True)



    def __str__(self):
            return self.Produto