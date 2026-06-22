from django.urls import path
from .views import admin_dashboard, staff_dashboard

urlpatterns = [
    path('admin-dashboard/', admin_dashboard),
    path('staff-dashboard/', staff_dashboard),
]