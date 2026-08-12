from rest_framework import generics, permissions, parsers
from rest_framework.response import Response

from apps.user.permissions import IsSeller, IsMine
from .models import ProductImage, Product
from .serializers import ProductSerializer, ProductImageSerializer, CreateProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    parser_classes = [parsers.JSONParser, parsers.MultiPartParser, parsers.FileUploadParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateProductSerializer
        return ProductSerializer

    def get_permissions(self):
        if self.request.method in ["POST"]:
            return [IsSeller()]
        return [permissions.AllowAny()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        images = request.FILES.getlist("images")
        for image in images:
            ProductImage.objects.create(product=serializer.instance, image=image)

        headers = self.get_success_headers(serializer.data)
        return Response(ProductSerializer(serializer.instance).data, status=201, headers=headers)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [IsMine()]