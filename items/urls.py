from django.urls import path
from . import views

urlpatterns = [
    path('',      views.item_list,   name='item-list'),
    path('<int:pk>/', views.item_detail, name='item-detail'),
]