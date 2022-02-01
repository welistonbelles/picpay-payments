from .models import Pedidos
import requests
import json

class Pedido:
    
    
    def generate_payment(request, form, *args, **kwargs):
        pedido = Pedidos.objects.all()

        if pedido.last():
            pedido = pedido.last().pedido
        else:
            pedido = 200

        url = 'https://appws.picpay.com/ecommerce/public/payments'
        headers = {
            "Content-Type": "application/json",
            "x-picpay-token": 'SEU TOKEN',
        }
        data = {
            "referenceId": int(pedido)+1,
            "callbackUrl": "https://picpay-pagamentos-django.herokuapp.com/api/v1/pedidos/",
            "returnUrl": "https://picpay-pagamentos-django.herokuapp.com/",
            "value": float(form.cleaned_data['value']),
            "expiresAt": "2023-05-01T16:00:00-03:00",
            "buyer": {
                "firstName": "Weliston",
                "lastName": "Belles",
                "document": "028.604.340-89",
                "email": "weliston2012@gmail.com",
                "phone": "+55 53 99999-2129"
            }
        }
        req = requests.post(url=url, headers=headers, data=json.dumps(data, indent = 4))

        if req.status_code == 200:
            qrcode = (req.json()['qrcode']['content']).split('https')[1]
            newPedido = Pedidos(
                pedido = data['referenceId'],
                valor = data['value'],
                expireAt = data['expiresAt'][:10],
                status = 'Pendente',
                qrcode = f'https{qrcode}'
            )
            newPedido.save()
        else: 
            print(req.json())
        
        return req