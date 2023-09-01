from django.contrib.auth import get_user_model, logout
from django.http import HttpRequest, HttpResponse
# from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from .forms import SignUpForm
from .utils import auto_login

User = get_user_model()


class SignUpView(generic.CreateView):
    template_name = "auth/signup.html"
    model = User
    form_class = SignUpForm

    def post(self, request: HttpRequest) -> HttpResponse:
        result = super().post(request)
        username = request.POST.get("username")
        password = request.POST.get("password")
        auto_login(request, username=username, password=password)
        return result

    def get_success_url(self) -> str:
        return reverse("home_page")


class LoginView(generic.FormView):
    def post(self, request: HttpRequest) -> HttpResponse:
        pass


class LogoutView(generic.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass
