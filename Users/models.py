from enum import unique
from math import trunc

from django.db import models

# Create your models here.


class UsersModel(models.Model):
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=15, null=True, unique=True)

    def __str__(self):
        return str(self.name)