from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import InsereIpSerializer

import requests
import json

class InsereIp(viewsets.GenericViewSet ):
    ''' Essa View é criada para a busca de dados de um determinado IP '''

    queryset = IP.objects.all()
    serializer_class = InsereIpSerializer

    def create(self, request, *args, **kwargs):
        response = super(InsereIp, self)
        ip = IP.objects.filter().order_by('-id')[0]
        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/listaip/{0}'.format(ip))


class ListaInfoIp(APIView):
    ''' Essa View atende a função de solicitar a API Externa (IPAPI) os dados do IP inserido no Model e os converte em objeto Python/Json '''

    def get(self, request, format=None):
        response = {}
        ip = IP.objects.filter().order_by('-id')[0]
        # Make an external api request ( use auth if authentication is required for the external API)
        r = requests.get(f'https://ipapi.co/{ip}/json/')
        r_status = r.status_code
        # If it is a success
        if r_status == 200:
            # convert the json result to python object
            d1 = json.dumps(r.json())
            data = json.loads(d1)
            response['status'] = 200
            response['message'] = 'success'
            response['informations'] = data
        else:
            response['status'] = r.status_code
            response['message'] = 'error'
            response['informations'] = {}
        return Response(response)

class ListaDados(viewsets.ReadOnlyModelViewSet):
    ''' Esta view lista todos os IPs procurados '''

    queryset = IP.objects.all()
    serializer_class = InsereIpSerializer
    
