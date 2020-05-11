from django.db import models

class Menu(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length = 200)
    image = models.CharField(max_length = 500, null=True)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length = 500)
    description = models.TextField() 
    image = models.CharField(max_length = 500, null=True)
    price = models.FloatField(null=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.SET_NULL,related_name='menu', blank=True, null=True)
   
    def __str__(self):
        return self.name

class Location(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length = 500)
    address = models.TextField() 
    phone = models.CharField(max_length = 12)    
    image = models.CharField(max_length = 500, null=True)
   
    def __str__(self):
        return self.name