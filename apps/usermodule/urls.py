"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path
# from . import views

# urlpatterns = [
#    path('login/', views.loginUser, name="login"),
#    path('register/', views.registerUser, name="register"),
#    path("logout/", views.logoutUser, name="logout"),

#    ]

from django.contrib import admin
from django.urls import path
from .views import register, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/',register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
