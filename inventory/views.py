from django.http import HttpResponse
from accounts.decorators import admin_only, staff_only
from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from .forms import EquipmentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Equipment, Category, Supplier, BorrowRecord

@login_required
def equipment_list(request):
    query = request.GET.get('q')

    if query:
        equipments = Equipment.objects.filter(name__icontains=query)
    else:
        equipments = Equipment.objects.all()

    return render(request, 'inventory/equipment_list.html', {
        'equipments': equipments
    })

@staff_only
@admin_only
@login_required
def add_equipment(request):
    form = EquipmentForm()

    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')

    return render(request, 'inventory/equipment_form.html', {
        'form': form
    })

@staff_only
@admin_only
@login_required
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, id=pk)
    form = EquipmentForm(instance=equipment)

    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')

    return render(request, 'inventory/equipment_form.html', {
        'form': form
    })

@admin_only
@login_required
def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, id=pk)

    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')

    return render(request, 'inventory/equipment_delete.html', {
        'equipment': equipment
    })

@staff_only
@login_required
def borrow_equipment(request, pk):
    equipment = Equipment.objects.get(id=pk)

    if equipment.quantity > 0:
        BorrowRecord.objects.create(
            equipment=equipment,
            user=request.user,
            quantity=1,
            is_returned=False
        )

        equipment.quantity -= 1
        equipment.status = 'borrowed'
        equipment.save()

    return redirect('equipment_list')

@staff_only
@login_required
def return_equipment(request, pk):
    equipment = Equipment.objects.get(id=pk)

    borrow = BorrowRecord.objects.filter(
        equipment=equipment,
        is_returned=False
    ).last()

    if borrow:
        borrow.is_returned = True
        borrow.date_returned = timezone.now()
        borrow.save()

        equipment.quantity += 1
        equipment.status = 'available'
        equipment.save()

    return redirect('equipment_list')
