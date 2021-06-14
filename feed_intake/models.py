from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models,CASCADE)
    name = models.CharField(max_length=200, numm=True)
    email = models.CharField(max_length=200, numm=True)
    date_created = models.DateTimeField(auto_now_add=True, numm=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    options = (
        ('breakfast','breakfast')
        ('lunch','lunch')
        ('snacks','snacks')
        ('dinner','dinner')
    )
    name = models.CharField(max_length=50,choices=options)

    def __str__(self):
        return self.name

class Food_items(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.name

#For User Page

class User_food_items(models.Model):
    customer = models.ManyToManyField(Customer, blank=True)
    food_items = models.ManyToManyField(Food_items)