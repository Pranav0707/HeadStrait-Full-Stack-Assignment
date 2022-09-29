from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField(blank=True,null=True)
    images=models.ImageField(upload_to="static/images/",null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)


    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Categories"       



class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=55,null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    slug=models.SlugField(null=True,blank=True)
    images=models.ImageField(upload_to="static/images/",null=True,blank=True)
    price=models.PositiveIntegerField(default=1)
    created_on=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField(auto_now_add=True)
    items=models.PositiveIntegerField()


    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
       self.slug=slugify(self.product_name)
       super(Product, self).save(*args, **kwargs) # Call the real save() method
    
