from django.db import models

# Create your models here.
class Workstation(models.Model):
    system_user = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50)
    system_brand = models.CharField(max_length=10)
    system_type = models.CharField(max_length=10)
    system_model = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.system_user