from django.http import HttpResponse
import datetime
from .models import *
from .serializers import *
from rest_framework import routers, serializers, viewsets 
from .serializers import CustomersSerializer
from rest_framework import generics
from rest_framework import status, pagination, mixins
from rest_framework.response import Response
class UserViewSet(generics.GenericAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    def get(self, request, format='json'):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    def post(self, request, format='json'):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        # Get object with this pk
        customer = get_object_or_404(Customers.objects.all(), pk=pk)
        customer.delete()
        return Response({"message": "customer with id `{}` has been deleted.".format(pk)},status=204)
    def put(self, request, pk):
        saved_customer = get_object_or_404(Customers.objects.all(), pk=pk)
        data = request.data.get('customer')
        serializer = CustomersSerializer(instance=saved_customer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            customer_saved = serializer.save()
        return Response({"success": "Customer '{}' updated successfully".format(customer_saved.title)})
    

        

