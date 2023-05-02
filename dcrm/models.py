from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")