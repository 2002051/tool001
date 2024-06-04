from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from www import models


# Create your views here.
class LoginModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["username", "password"]


def login(request):
    if request.method == "GET":
        form = LoginModelForm()
        return render(request, "login.html", {"form": form})
    print('request.POST', request.POST)
    form = LoginModelForm(data=request.POST)
    if not form.is_valid():
        return render(request, "login.html", {"form": form})
    user_object = models.User.objects.filter(**form.cleaned_data).first()
    if not user_object:
        form.add_error("password", "用户名或者密码错误")
    request.session["userinfo"] = {"id": user_object.id, "username": user_object.username,
                                   "isSuper": user_object.is_super}
    return redirect("home")


def home(request):
    return HttpResponse("主页")


def computer(request):
    return HttpResponse("ok")


def computer_add(request):
    return HttpResponse("ok")


def computer_edit(request):
    return HttpResponse("ok")


def computer_del(request):
    return HttpResponse("ok")


def order(request):
    return HttpResponse("ok")


def order_add(request):
    return HttpResponse("ok")


def order_edit(request):
    return HttpResponse("ok")


def order_del(request):
    return HttpResponse("ok")
