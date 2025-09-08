from django.contrib import admin
from django.urls import path, include
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),   # API endpoints: /api/produtos/...
    path('', views.index, name='index'),   # frontend simples
]
