from django import views
from django.http import JsonResponse
from django.shortcuts import render

from test01.forms import *


def index(request):
    return render(request, 'index.html')


class Register(views.View):
    def get(self, request):
        reg_form = RegisterForm()
        return render(request, 'register.html', {'form': reg_form})

    def post(self, request):
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            print('验证成功')
            return render(request, 'register.html', {'form': reg_form})
        else:
            print('验证失败')
            print(reg_form.errors.as_json())
            return render(request, 'register.html', {'form': reg_form})


class RegisterAjax(views.View):
    def get(self, request):
        reg_form = RegisterForm()
        return render(request, 'register_ajax.html', {'form': reg_form})

    def post(self, request):
        print(request.POST)
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            return JsonResponse(data={'msg': 'ok ok ok'})
        return JsonResponse(data=reg_form.errors)
