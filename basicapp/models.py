from django.db import models

# Create your models here.

class employees(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')
    description = models.TextField(max_length=500)
    phonenumber = models.CharField(max_length=12 , blank=True)
    email = models.EmailField(max_length=200 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return self.firstname