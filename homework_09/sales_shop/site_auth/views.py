from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import LoginView as LoginViewGeneric
from django.contrib.auth.views import LogoutView as LogoutViewGeneric
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .tasks import welcome_new_user
from .forms import AuthenticationForm, UserCreationForm


class LogonView(LoginViewGeneric):
    template_name = "site_auth/login.html"
    form_class = AuthenticationForm
    next_page = reverse_lazy("site_auth:about-me")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("site_auth:about-me")


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "site_auth/register.html"
    success_url = reverse_lazy("site_auth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        # user: AbstractUser =self.object
        welcome_new_user.delay(self.object.pk)

        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password1")

        user:AbstractUser= authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response
    
