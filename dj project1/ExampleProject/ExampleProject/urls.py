"""ExampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from VVITApp import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('g/',views.demo),
    path('k/<str:n>/',views.greet),
    path('gh/<str:a>/<int:b>/',views.stdnt),
    path('gs/<str:a>/',views.dis),
    path('eh/<str:n>/<int:a>/',views.sam),
    path('p/<str:a>/',views.fln),
    path('t/<str:a>/<int:b>/<str:c>/<int:d>/',views.ssm),
    path('ty/<str:a>',views.abbs),
    path('ts/<str:a>/',views.ass),
    path('st/<str:a>/<int:b>/<str:c>/',views.emp),
    path('ss/',views.pps),
    path('',include('BSApp.urls')),
]
