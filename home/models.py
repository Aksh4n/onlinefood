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
    item1 = models.CharField(max_length=200, null=True , blank=True)
    q1 = models.IntegerField(null=True , blank=True)
    item2 = models.CharField(max_length=200, null=True , blank=True)
    q2 = models.IntegerField(null=True , blank=True)
    item3 = models.CharField(max_length=200, null=True , blank=True)
    q3 = models.IntegerField(null=True , blank=True)
    item4 = models.CharField(max_length=200, null=True , blank=True)
    q4 = models.IntegerField(null=True , blank=True)
    date_ordered = models.DateTimeField(default=now)
    date_needed = models.CharField(max_length=200 , null=True, blank=True)
    msg = models.TextField(max_length=1000, null=True,blank=True)
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

class Order2(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    item1 = models.CharField(max_length=200, null=True , blank=True)
    q1 = models.IntegerField(null=True , blank=True)
    item2 = models.CharField(max_length=200, null=True , blank=True)
    q2 = models.IntegerField(null=True , blank=True)
    item3 = models.CharField(max_length=200, null=True , blank=True)
    q3 = models.IntegerField(null=True , blank=True)
    item4 = models.CharField(max_length=200, null=True , blank=True)
    q4 = models.IntegerField(null=True , blank=True)
    date_ordered = models.DateTimeField(default=now)
    date_needed = models.CharField(max_length=200 , null=True, blank=True)
    msg = models.TextField(max_length=1000, null=True,blank=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)



    def __str__(self):

        return self.subject  