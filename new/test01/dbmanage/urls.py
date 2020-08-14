from dbmanage import views
from django.urls import path
urlpatterns =[ path("list",views.list,name="dbmanage-home"),]
