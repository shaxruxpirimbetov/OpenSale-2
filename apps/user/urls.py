from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view()),
    path("<slug:username>/", views.UserDetailAPIView.as_view()),
]