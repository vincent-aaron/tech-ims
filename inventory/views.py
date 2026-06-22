from django.http import HttpResponse
from accounts.decorators import admin_only, staff_only


@admin_only
def admin_dashboard(request):
    return HttpResponse("Admin Dashboard")


@staff_only
def staff_dashboard(request):
    return HttpResponse("Staff Dashboard")