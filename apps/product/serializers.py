from rest_framework import serializers
from .models import Product, ProductImage
from apps.user.serializers import ResponseUserSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    user = ResponseUserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "description", "price"]