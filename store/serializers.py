from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'nome', 'preco', 'estoque', 'created_at', 'updated_at']

    def validate_preco(self, value):
        if value < 1:
            raise serializers.ValidationError("Preço deve ser no mínimo 1")
        return value

    def validate_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("Estoque não pode ser negativo")
        return value
