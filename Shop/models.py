from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    image = models.ImageField(upload_to='category/', default="")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('Shop:Product_category', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products_category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length= 200,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    available = models.BooleanField(default= True)
    description = models.TextField(blank=True)
    product_information = models.TextField(blank=True)

    class Meta:
        ordering = ('name',) 
        index_together = (('id','slug'),)

    def get_absolute_url(self):
        return reverse('Shop:Product_Detail',args=[self.id,self.slug])

    def __str__(self):
        return self.name
    
    
class Store(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100,unique= True)
    owner = models.OneToOneField(User, on_delete= models.CASCADE, related_name='store_owner')

    def __str__(self):
        return self.name

