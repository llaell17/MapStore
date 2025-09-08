from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField(validators=[MinValueValidator(1.0)])
    estoque = models.IntegerField(validators=[MinValueValidator(0)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produtos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f})"
