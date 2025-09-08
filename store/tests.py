from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_product(self):
        data = {'nome': 'Caneca', 'preco': 15.5, 'estoque': 10}
        res = self.client.post('/api/produtos/', data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', res.data)
        self.assertEqual(Product.objects.count(), 1)

    def test_create_invalid_negative_stock(self):
        data = {'nome': 'ErroEstoque', 'preco': 10, 'estoque': -5}
        res = self.client.post('/api/produtos/', data, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_products(self):
        Product.objects.create(nome='P1', preco=5.0, estoque=2)
        res = self.client.get('/api/produtos/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsInstance(res.data, list)

