from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

# View para o frontend (template)
def index(request):
    return render(request, 'store/index.html')

# API (ViewSet simples)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    # Exemplo: ao deletar, retornamos mensagem customizada
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Produto deletado'}, status=status.HTTP_200_OK)
