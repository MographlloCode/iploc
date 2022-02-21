from rest_framework import serializers

from .models import *
from .views import *

class InsereIpSerializer(serializers.ModelSerializer):
    ''' Serializador do Modelo IP '''
    class Meta:
        model = IP
        fields = ['id','ip']