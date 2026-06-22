from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # Admins
        admins = ["admin1", "admin2"]
        for username in admins:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    password="password123",
                    role="admin"
                )

        # Staff (NO staff1)
        staff = ["staff2", "staff3", "staff4", "staff5"]
        for username in staff:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    password="password123",
                    role="staff"
                )

        # Viewer
        if not User.objects.filter(username="view1").exists():
            User.objects.create_user(
                username="view1",
                password="password123",
                role="viewer"
            )

        self.stdout.write(self.style.SUCCESS("Users seeded successfully"))