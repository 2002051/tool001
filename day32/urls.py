"""
URL configuration for day32 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from www import views

urlpatterns = [
    path("login",views.login,name="login"),
    path("home",views.home,name="home"),
    # path('admin/', admin.site.urls),
    path("computer/",views.computer,name="cpmputer"),
    path("computer/add/",views.computer_add,name="cpmputer_add"),
    path("computer/edit/<int:id>/",views.computer_edit,name="cpmputer_edit"),
    path("computer/del/<int:id>/",views.computer_del,name="cpmputer_del"),

    path("order/", views.order, name="cpmputer"),
    path("order/add/", views.order_add, name="order_add"),
    path("order/edit/<int:id>/", views.order_edit, name="order_edit"),
    path("order/del/<int:id>/", views.order_del, name="order_del"),
]
