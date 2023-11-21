from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from . import views

urlpatterns = [
    # REFRESH AND ACCESS TOKEN URL
    path('token/', views.MyTokenObtainPairView.as_view()),

    # REFRESH TOKEN URL
    path('token/refresh/', TokenRefreshView.as_view()),

    # REGISTER URL PAGE
    path('register/', views.RegisterView.as_view()),

    # DASHBOARD URL PAGE
    path('dashboard/', views.dashboard),

    # TEST URL PAGE
    path('test/', views.testEndPoint, name='test'),

    # TO DISPLAY ALL THE ROUTES IN OUR API
    path('', views.getRoutes),
]