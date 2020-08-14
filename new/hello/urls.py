from hello import views
from django.urls import path
urlpatterns=[path("form/",views.form,name="form"),path("template/", views.template, name="template"),]

