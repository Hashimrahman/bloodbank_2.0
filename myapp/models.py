from django.db import models

# Create your models here.

from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
