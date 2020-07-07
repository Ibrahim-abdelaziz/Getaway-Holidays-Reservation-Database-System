from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions 
from .model.client import Client
from .serializers import ClientSerializer
# Create your views here.



class ClientView(ModelViewSet):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer
    # permission_classes = (permissions.IsAuthenticated,)



class DeleteAccount(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        try:

            request.user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return e   






