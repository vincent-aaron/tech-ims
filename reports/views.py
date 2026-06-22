from django.shortcuts import render
from inventory.models import Equipment, BorrowRecord


def report_dashboard(request):
    equipment = Equipment.objects.all()
    borrows = BorrowRecord.objects.all()

    return render(request, 'reports/dashboard.html', {
        'equipment': equipment,
        'borrows': borrows
    })