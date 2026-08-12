from django.shortcuts import render
from django.views import View
from rest_framework import permissions


class Index(View):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        return render(request, "index.html")