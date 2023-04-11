from django.db import models
#from django.contrib.auth.models import AbstractUser
from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    # ticket_price = models.FloatField()
    # description = models.TextField()
    def __str__(self):
        return self.name

class Booking(models.Model):
    #event = models.ForeignKey(Event.name, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    regno=models.CharField(max_length=15)
    mno=models.IntegerField()
    email = models.EmailField()
    eventname=models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regno = models.CharField(max_length=15)
    upi_id = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=50)
    payment_screenshot = models.ImageField(upload_to='screenshots/')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.regno}"

#class User(AbstractUser):
    # add additional fields here
  #  email = models.EmailField(unique=True)

class Contact(models.Model):
    name1 = models.CharField(max_length=50)
    email1 = models.CharField(max_length=30)
    subject1 = models.CharField(max_length=100)
    message1 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name1