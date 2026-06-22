from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Equipment(models.Model):

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('damaged', 'Damaged'),
        ('maintenance', 'Maintenance'),
    )

    name = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=100, unique=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"
    
class BorrowRecord(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(null=True, blank=True)

    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.equipment.name} borrowed by {self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.is_returned:
            self.equipment.status = 'borrowed'
        else:
            self.equipment.status = 'available'

        self.equipment.save()