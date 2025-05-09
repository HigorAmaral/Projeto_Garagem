from rest_framework.serializers import ModelSerializer
from core.models import Acessorio

class AcessorioSerializer(ModelSerializer):

    class Meta:
        model = Acessorio
        fields = ('id', 'descricao')
        read_only_fields = ('id',)