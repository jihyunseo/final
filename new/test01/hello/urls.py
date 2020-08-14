from hello import views
from django.urls import path # add
urlpatterns = [
path("home", views.home, name="hello-home"),
path("intro",views.intro,name="hello-intro"),

]

