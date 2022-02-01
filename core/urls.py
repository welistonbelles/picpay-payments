from ast import Index
from django.urls import path
from .views import IndexView, PedidoViewSet


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/v1/pedidos/', PedidoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
]