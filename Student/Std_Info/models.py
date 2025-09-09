from django.db import models

# Create your models here.
class StdInfo(models.Model):
    std_name = models.CharField(max_length=100)
    std_age = models.IntegerField()
    std_city = models.CharField(max_length=100)
    std_email = models.EmailField()
    std_phone_number = models.CharField(max_length=15)
    std_address = models.TextField()

    def __str__(self):
        return self.name