"""banking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.app1, name='app1')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='app1')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login_page"),
    path('homepage/', views.homepage, name="homepage"),
    path("customer/", views.view_customer, name="customer"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("transfer/", views.transfer, name="transfer"),
    path("transactions/", views.transactions, name="transactions")
]
