from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cutlery/', views.cutlery_index, name='cutlery_index'),
    path('cutlery/<int:cutlery_id>/', views.cutlery_detail, name='detail'),
    path('cutlery/<int:cutlery_id>/add_sharpen/', views.add_sharpen, name='add_sharpen'),
    path('cutlery/<int:cutlery_id>/assoc_prep/<int:prep_id>/', views.assoc_prep, name='assoc_prep'),
    path('cutlery/<int:cutlery_id>/remove_prep/<int:prep_id>/', views.remove_prep, name='remove_prep')
]