from django.db import models

# Create your models here.

class Produto(models.Model):
    SKU = models.IntegerField()
    Produto = models.TextField()
    Dados_Complementares = models.TextField()
    UM = models.CharField(max_length=200)
    Categoria = models.TextField()

    def __str__(self):
        return self.Produto