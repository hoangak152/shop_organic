from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    title = models.CharField(max_length=264, unique=True)
    price= models.IntegerField()
    def __str__(self):
        return f"{self.title}\n{self.price}"
class Category(models.Model):
    name = models.CharField(max_length=264, unique=True)
    title = models.CharField(max_length=264, unique=True)
    description= models.TextField(unique=True)
    content= models.TextField(unique=True)
    image = models.TextField()
    def __str__(self):
        return self.title
class Fruit(models.Model):
    name = models.CharField(max_length=264, unique=True)
    price= models.IntegerField()
    title = models.CharField(max_length=264, unique=True)
    image = models.TextField()
    def __str__(self):
        return self.name
