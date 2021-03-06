"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#https://django-background-tasks.readthedocs.io/en/latest/

from django.contrib import admin
from django.urls import path
from django.urls import include
# from crawling.crawling_tasks import task_hello # add
from crawling.crawling_tasks import task_crawling_naver
# task_hello(schedule=5, repeat=5)
task_crawling_naver(schedule=0, repeat=3600)

urlpatterns = [
    path("hello/", include("hello.urls")),
    path("dbmanage/", include("dbmanage.urls"))
]
