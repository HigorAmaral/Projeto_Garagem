from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer  

from core.models import Veiculo, Acessorio, Cor, Modelo
from core.serializers.veiculo import VeiculoSerializer

class VeiculoViewSet(ModelViewSet):  
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer  