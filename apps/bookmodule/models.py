from django.db import models

# Create your models here.
class Book(models.Model): # database scheme
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)


class Address(models.Model):
    city = models.CharField(max_length = 50)
    
#class Student(models.Model):
    # name = models.CharField(max_length = 50)
    # age = models.IntegerField()
    # address = models.ForeignKey(Address, on_delete=models.PROTECT)

class Card(models.Model):
     card_number = models.CharField(max_length=20, unique=True)

class department(models.Model):
     name = models.CharField(max_length = 50)

class course(models.Model):   
     title = models.CharField(max_length = 50)
     code = models.SmallIntegerField(default = 1)

class Student(models.Model):
     name = models.CharField(max_length=300)
     card = models.OneToOneField(Card, on_delete = models.PROTECT)
     department = models.ForeignKey(department, on_delete=models.PROTECT)
     course = models.ManyToManyField(course)


