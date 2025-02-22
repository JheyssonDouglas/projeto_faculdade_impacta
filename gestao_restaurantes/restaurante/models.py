from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Stock(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
