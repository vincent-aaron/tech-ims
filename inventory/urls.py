from django.urls import path
from .views import (
    equipment_list,
    add_equipment,
    edit_equipment,
    delete_equipment
)

urlpatterns = [
    path('equipment/', equipment_list, name='equipment_list'),
    path('equipment/add/', add_equipment, name='add_equipment'),
    path('equipment/edit/<int:pk>/', edit_equipment, name='edit_equipment'),
    path('equipment/delete/<int:pk>/', delete_equipment, name='delete_equipment'),
]