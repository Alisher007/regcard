from django.db import models

class Customer(models.Model):
     surname = models.CharField(max_length=500)
     firstname = models.CharField(max_length=500)
     address = models.CharField(max_length=500)
     zip = models.CharField(max_length=500)
     state = models.CharField(max_length=500)
     city = models.CharField(max_length=500)
     country = models.CharField(max_length=500)
     telephone = models.CharField(max_length=500)
     email = models.EmailField()
     arrival = models.CharField(max_length=500)
     departure = models.CharField(max_length=500)
     room = models.CharField(max_length=500)
     adults = models.CharField(max_length=500)
     children = models.CharField(max_length=500)
     room_type = models.CharField(max_length=500)
     rate = models.CharField(max_length=500)
     reservation = models.CharField(max_length=500)
     payment_method = models.CharField(max_length=500)
     newspaper = models.BooleanField(default=False)
     janews = models.BooleanField(default=False)
     discovery = models.BooleanField(default=False)
     loyalty = models.BooleanField(default=False)
     signature = models.ImageField(default='default.png', blank=True)

     def __str__(self):
        return self.surname
