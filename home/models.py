from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    info = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
from django.utils.timezone import now
class Order(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    items = models.TextField(max_length=1000)
    date_ordered = models.DateTimeField(default=now)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return str(self.name)

    #@property
    #def get_cart_total(self):
        #orderitems = self.orderitem_set.all()
        #total = sum([item.get_total for item in orderitems])
        #return total    
    #@property
    #def get_cart_items(self):
        #orderitems = self.orderitem_set.all()
        #total = sum([item.quantity for item in orderitems])
        #return total        
    #@property
    #def get_cart_options(self):
        #orderitems = self.orderitem_set.all()
        #total = (item.product.option_set.all() for item in orderitems)
        #return total            
