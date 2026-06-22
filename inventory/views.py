from django.http import HttpResponse
from accounts.decorators import admin_only, staff_only
from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from .forms import EquipmentForm
from django.contrib.auth.decorators import login_required

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
