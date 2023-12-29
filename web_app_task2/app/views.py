from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from app import forms, models


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render(
            request, "landing.html", {"car_post": models.VehiclePost.objects.all()}
        )


class PostVehicle(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request, "post-vehicle.html", {"post_form": forms.PostVehicleForm()}
        )

    def post(self, request):
        form = forms.PostVehicleForm(data=request.POST)
        if form.is_valid():
            car_img = form.cleaned_data["car_img"]
            year = form.cleaned_data["year"]
            make = form.cleaned_data["make"]
            model = form.cleaned_data["model"]
            mileage = form.cleaned_data["mileage"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]

            models.VehiclePost.submit_vehicle_post(
                car_img, year, make, model, mileage, price, description
            )
            return redirect("landing")
        else:
            return render(request, "post-vehicle.html", {"post_form": form})


class VehicleSale(LoginRequiredMixin, View):
    def get(self, request, id):
        return render(
            request,
            "car-page.html",
            {"car_post": models.VehiclePost.objects.get(id=id)},
        )


class BuyingVehicle(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request, "buy-vehicle.html", {"buy_vehicle": forms.BuyingCarForm()}
        )

    def post(self, request):
        form = forms.BuyingCarForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            z_code = form.cleaned_data["z_code"]
            p_number = form.cleaned_data["p_number"]

            models.BuyVehicle.submit_vehicle_purchase(
                name, street, city, state, z_code, p_number
            )
            return redirect("receipt")
        else:
            return render(request, "buy-vehicle.html", {"buy-vehicle": form})


class VehicleReceipt(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request, "receipt.html", {"car_receipt": models.BuyVehicle.objects.all()}
        )


class ViewingReceipt(LoginRequiredMixin, View):
    def get(self, request, id):
        return render(
            request,
            "receipt-page.html",
            {"read_receipt": models.BuyVehicle.objects.get(id=id)},
        )


class Login(LoginView):
    template_name = "login.html"


class Logout(LogoutView):
    template_name = "logout.html"


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class Register(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("landing")
    template_name = "register.html"

    def form_valid(self, form):
        login(self.request, form.save())
        return super().form_valid(form)


def contact_us(request):
    if request.method == "POST":
        form = forms.ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = forms.ContactMessageForm()

    return render(request, "contact_us.html", {"form": form})


def contact_success(request):
    return render(request, "contact_success.html")
