from rest_framework.serializers import ModelSerializer
from ncm.models import Ncm

class NcmSerializer(ModelSerializer):
    class Meta:
        model = Ncm
        fields = "__all__"