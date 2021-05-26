from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id',
                  'Name',
                  'Family',
                  'Address',
                  'Zip_Code',
                  'Phone',
                  'Phone_Whats_App',
                  'Pic',
                  'Size_Of_Product',
                  'Description',
                  'Debt_Rate',
                  'Type_Of_Product',
                  'Type_Of_Send',
                  'Tipax_Code']


class CustomersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = [
            #   'id',
            'Name',
            'Family',
            'Address',
            'Zip_Code',
            'Phone',
            'Phone_Whats_App',
            'Pic',
            'Size_Of_Product',
            'Description',
            'Debt_Rate',
            'Type_Of_Product',
            'Type_Of_Send',
            'Tipax_Code']
