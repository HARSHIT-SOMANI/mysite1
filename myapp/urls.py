from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('', views.index,name=''),
    path('createUser',views.createUser),
    path('updateUser/<str:input>/',views.updateUser),
    path('deleteUser/<str:input>/',views.deleteUser),
    path('getUser',views.getUser),

]
