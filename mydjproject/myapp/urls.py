from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage),
    path("add-Student",views.addStudent),
    path("display-student",views.displayStudent)
]