from django.contrib import admin
from .models import Category, Supplier, Equipment, BorrowRecord


admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Equipment)
admin.site.register(BorrowRecord)