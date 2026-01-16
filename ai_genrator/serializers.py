from rest_framework import serializers
from .models import ProductDetials


class ProductDetialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetials
        fields = '__all__'
        
class BulkProductDetialsSerializer(serializers.Serializer):
    product_name=serializers.CharField(max_length=200)
    material=serializers.CharField(max_length=200)
    color=serializers.CharField(max_length=100)
    audience=serializers.CharField(max_length=200)
    description=serializers.CharField()