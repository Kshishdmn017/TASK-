from django.contrib import admin

from .models import BuyVehicle, VehiclePost

# Register your models here.


@admin.register(VehiclePost)
class VehiclePostAdmin(admin.ModelAdmin):
    list_display = ("car_img", "year", "make", "model", "mileage", "price")
    search_fields = ("make", "model")
    list_filter = ("year",)


@admin.register(BuyVehicle)
class BuyVehicleAdmin(admin.ModelAdmin):
    list_display = ("name", "street", "city", "state", "z_code", "p_number")
    search_fields = ("name", "city", "state")
    list_filter = ("state", "z_code")


# Register your models here.
