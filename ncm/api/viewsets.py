from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ncm.api.serializers import NcmSerializer
from ncm.models import Ncm

class NcmViewset(ModelViewSet):
    queryset = Ncm.objects.all()
    serializer_class = NcmSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(data={"message": "Requisição não permitida."}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        return Response(data={"message": "Requisição não permitida."}, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        return Response(data={"message": "Requisição não permitida."}, status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        return Response(data={"message": "Requisição não permitida."}, status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        return Response(data={"message": "Requisição não permitida."}, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):        
        instance = Ncm.objects.filter(codigo=pk).first()

        if not instance:
            return Response(data={"message": "NCM não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
