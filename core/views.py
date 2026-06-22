from django.shortcuts import render
from inventory.models import Equipment, BorrowRecord


def dashboard(request):
    total_equipment = Equipment.objects.count()
    available = Equipment.objects.filter(status='available').count()
    borrowed = Equipment.objects.filter(status='borrowed').count()
    damaged = Equipment.objects.filter(status='damaged').count()

    recent_borrows = BorrowRecord.objects.select_related('equipment', 'user').order_by('-date_borrowed')[:5]

    context = {
        'total_equipment': total_equipment,
        'available': available,
        'borrowed': borrowed,
        'damaged': damaged,
        'recent_borrows': recent_borrows,
    }

    return render(request, 'core/dashboard.html', context)