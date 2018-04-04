from django import forms
from django.contrib.auth import authenticate, login
from django.db import models
from django.utils import timezone

class BigCategory(models.Model):
    categories = models.CharField(max_length=20,default="bigcategory")
    category_name = models.CharField(max_length=20,default="bigcategory")
    def __str__(self):
        return self.category_name

class Category(models.Model):
    bigcategory = models.ForeignKey(BigCategory,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=20,default="category")
    categories = models.CharField(max_length=20,default="category")
    def __str__(self):
        return self.category_name
class Specify(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image',blank=True,null=False )            
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now, blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        