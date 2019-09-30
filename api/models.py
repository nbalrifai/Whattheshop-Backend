from django.db import models
from django.contrib.auth.models import User

class CoffeeBean(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    origin = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField (null = True, blank = True)
    packetize = models.CharField(max_length=120)
    price = models.DecimalField (max_digits = 4, decimal_places = 2) 

    def __str__(self):
        return self.name

# Map: location
# Currency 

# 3
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    totalPrice = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    completed_order = models.BooleanField(default=False)

    def __str__(self):
    	return str(self.user)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    cofeeBean = models.ForeignKey(CoffeeBean, on_delete=models.CASCADE, related_name="order_items")
    Quant = models.PositiveIntegerField(default=1)

 # class CoffeeBeanOrder(models.Model):
# 	cofeeBean = models.ManyToOne(CoffeeBean, on_delete=models.CASCADE)
# 	Quant= models.IntegerField(max_length=4)
# 	totalPrice = models.IntegerField(max_length=4)
# 	origin = models.CharField(max_length=120)

