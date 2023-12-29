"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.LandingPage.as_view(), name="landing"),
    path("posting-vehicle", views.PostVehicle.as_view(), name="post-vehicle"),
    path("car-page/<id>/", views.VehicleSale.as_view(), name="car-page"),
    path("buy-vehicle", views.BuyingVehicle.as_view(), name="buy-vehicle"),
    path("receipt", views.VehicleReceipt.as_view(), name="receipt"),
    path("receipt-page/<id>/", views.ViewingReceipt.as_view(), name="view-receipt"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("contact/", views.contact_us, name="contact_us"),
    path("contact/success/", views.contact_success, name="contact_success"),
]
