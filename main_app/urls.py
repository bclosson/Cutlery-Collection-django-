from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Static Routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Cutlery Routes
    path('cutlery/index/', views.cutlery_index, name='cutlery_index'),
    path('cutlery/new/', views.add_cutlery, name='add_cutlery'),
    path('cutlery/<int:cutlery_id>/delete/', views.delete_cutlery, name='delete_cutlery'),
    path('cutlery/<int:cutlery_id>/edit/', views.edit_cutlery, name='edit_cutlery'),
    path('cutlery/<int:cutlery_id>/', views.cutlery_detail, name='detail'),
    # Sharpen Routes
    path('cutlery/<int:cutlery_id>/add_sharpen/', views.add_sharpen, name='add_sharpen'),
    # Prep Routes
    path('cutlery/<int:cutlery_id>/assoc_prep/<int:prep_id>/', views.assoc_prep, name='assoc_prep'),
    path('cutlery/<int:cutlery_id>/remove_prep/<int:prep_id>/', views.remove_prep, name='remove_prep'),
    # Auth
    path('accounts/signup', views.signup, name="signup")
]