from django.db import models

# Create your models here.

class Product(models.Model):
    pname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=80)
    zip_code = models.IntegerField()
    mobile = models.CharField(max_length=11)
    date = models.DateField()
    message = models.TextField()
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.pname

