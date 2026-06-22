from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('viewer', 'Viewer'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')

    def is_admin(self):
        return self.role == 'admin'

    def is_staff_role(self):
        return self.role == 'staff'

    def is_viewer(self):
        return self.role == 'viewer'
    
    @property
    def is_admin_role(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_staff_role(self):
        return self.role == 'staff'

    @property
    def is_viewer_role(self):
        return self.role == 'viewer'
