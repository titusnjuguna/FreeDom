from django.db import models
from django.urls import reverse
from Users.models import Seller


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('Shop:Product_List_category',args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length= 200,db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    available = models.BooleanField(default= True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',) 
        index_together = (('id','slug'),)

    def get_absolute_url(self):
        return reverse('Shop:Product_Detail',args=[self.id,self.slug])

    def __str__(self):
        return self.name
    
    
class Store(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100,unique= True)
    owner = models.OneToOneField(Seller, on_delete= models.CASCADE, related_name='store_owner')

    def __str__(self):
        return self.name

