from email import header
from re import M
from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from .forms import DonationForm
from .models import Pedidos
from .pedidos import Pedido
from .serializers import PedidoSerializer
from django.urls import reverse_lazy
import requests
import threading

# DRF 
from rest_framework import viewsets, status
from rest_framework.response import Response

class IndexView(FormView):
    template_name = 'index.html'
    form_class = DonationForm
    success_url = reverse_lazy('index')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.generate_payment(request, form)
        else:
            return self.form_invalid(form)

    def get(self, request, data=None, *args, **kwargs):
        context = self.get_context_data()
        if data:
            context['pedido'] = {
                "referenceId": data['referenceId'],
                "qrcode": data['qrcode']['base64'],
            }
        context['pedidos'] = Pedidos.objects.order_by('-pedido')[:6]
        return self.render_to_response(context)

    def generate_payment(self, request, form, *args, **kwargs):
        req = Pedido.generate_payment(request, form, *args, **kwargs)
        data = req.json()
        if req.status_code == 200:
            return self.get(request, data, *args, **kwargs)

        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    

class PedidoViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Pedidos.objects.all()
    serializer_class = PedidoSerializer

    def list(self, request):
        return Response({})

    def create(self, request):
        if request.data.get('referenceId'):
            threading.Timer(3, self.validate_pedido, (request.data,)).start()
        return Response({}, status=status.HTTP_200_OK)
    
    def validate_pedido(self, data):
        url = f'https://appws.picpay.com/ecommerce/public/payments/{data["referenceId"]}/status'
        headers = {
            "Content-Type": "application/json",
            "x-picpay-token": 'SEU TOKEN',
        }
        req = requests.get(url=url, headers=headers)
        if req.status_code == 200:
            data = req.json()
            if data.get('status'):
                pedido = Pedidos.objects.filter(pedido=int(data['referenceId'])).first()
                if pedido:
                    if data['status'] == 'paid':
                        pedido.status = 'Aprovado'
                    elif data['status'] == 'refunded':
                        pedido.status = 'Reembolsado'
                    pedido.save()
                    threading.Timer(60, self.refound_pedido, (data,)).start()
                else:
                    print("Não achei este pedido.")
            else:
                print("Não achei o campo status")
        else:
            print("O status code não é 200")