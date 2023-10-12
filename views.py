from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import generics

from shServ.models import Slave, Guardian, GuardianCompany
from shServ.serializers import SlaveSerializer, GuardianCompanySerializer, GuardianSerializer


class SlaveAPIView(generics.ListAPIView):
    queryset = Slave.objects.all()
    serializer_class = SlaveSerializer


class GuardianAPIView(generics.ListAPIView):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer


class GuardianCompanyAPIView(generics.ListAPIView):
    queryset = GuardianCompany.objects.all()
    serializer_class = GuardianCompanySerializer


def home(request):
    return render(request, 'shServ/home.html')


def registration(request):
    return render(request, 'shServ/registration.html')


def authorization(request):
    return render(request, 'shServ/authorization.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'shServ/registration.html'
    success_url = reverse_lazy('authorization')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'shServ/authorization.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('authorization')
