from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from innovalaUApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('estudiante/', views.UserCreateView.as_view()),
    path('estudiante/<int:pk>/', views.UserDetailView.as_view()),
]