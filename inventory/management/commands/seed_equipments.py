from django.core.management.base import BaseCommand
from inventory.models import Category, Supplier, Equipment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # Categories
        categories = ["Desktop", "Monitor", "Keyboard", "Mouse", "Printer"]

        cat_objs = {}
        for c in categories:
            obj, _ = Category.objects.get_or_create(name=c)
            cat_objs[c] = obj

        # Supplier
        supplier, _ = Supplier.objects.get_or_create(
            name="Tech Supply Inc"
        )

        # Equipment list
        items = [
            ("Dell Desktop PC", "PC-001", "Desktop"),
            ("HP Monitor 24inch", "MN-001", "Monitor"),
            ("Logitech Keyboard", "KB-001", "Keyboard"),
            ("Logitech Mouse", "MS-001", "Mouse"),
            ("Epson Printer L3110", "PR-001", "Printer"),
        ]

        for name, serial, cat in items:
            Equipment.objects.get_or_create(
                name=name,
                serial_number=serial,
                category=cat_objs[cat],
                supplier=supplier,
                quantity=5,
                status="available"
            )

        self.stdout.write(self.style.SUCCESS("Equipment seeded successfully"))