from django.db import models
from django.contrib.auth.models import User

class detail(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete="DO_NOTHING")
    domicilio = models.TextField(max_length=200, blank=True)
    telefono = models.TextField(max_length=50, blank=True)
