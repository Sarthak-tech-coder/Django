from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('return',views.logic, name="logic"),
    path('delete/<name_place>/', views.delete_city, name="delete_place"),
    path('nasapi', views.nasa,name= 'nasa')]