from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    
    
    
    unit_choices = (
        ('250gm','250gm'),
        ('500gm','500gm'),
        ('1kg','1kg'),
    )
    
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique= True)
    description = models.TextField(max_length=500, blank= True)
    price = models.IntegerField()
    product_images = models.ImageField(upload_to='photos/products/',blank= True)
    product_images_1 = models.ImageField(upload_to='photos/products/',blank= True)
    product_images_2 = models.ImageField(upload_to='photos/products/',blank= True)
    product_images_3 = models.ImageField(upload_to='photos/products/',blank= True)
    stock = models.IntegerField()
    unit = models.CharField(choices=unit_choices,max_length=10,null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug])
    
    def __str__(self):
        return self.product_name