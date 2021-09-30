
from django.urls import path
from . import views

urlpatterns = [
    
    path("addUser",views.addUser,name="addUser"),
    path("addSomething",views.addSomething,name="addSomething"),
    path("addNew/<someNumber>",views.addNew,name="addNew"),

]