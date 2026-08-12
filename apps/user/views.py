from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer
from .permissions import IsMine, IsMe

User = get_user_model()

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    # def get_permissions(self):
    #     if self.request.method == "POST":
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [IsMe()]