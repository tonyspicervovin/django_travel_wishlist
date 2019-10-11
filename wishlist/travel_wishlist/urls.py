from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'), #home papge
    path('visited', views.places_visited, name='places_visited'), #visited tab
    path('was_visited', views.place_was_visited, name='place_was_visited')

]