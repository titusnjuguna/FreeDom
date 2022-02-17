from pickletools import read_long4
from py_compile import main
from rest_framework import serializers
from ..models import Product,Category


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ['created','updated']
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True,read_only= True)
    class Meta:
        model = Category
        exclude = ['slug',]
