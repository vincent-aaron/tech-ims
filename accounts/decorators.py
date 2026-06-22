from django.shortcuts import redirect
from django.http import HttpResponse


def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        return HttpResponse("Unauthorized - Admin only")
    return wrapper


def staff_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role in ['admin', 'staff']:
            return view_func(request, *args, **kwargs)
        return HttpResponse("Unauthorized - Staff only")
    return wrapper


def viewer_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper