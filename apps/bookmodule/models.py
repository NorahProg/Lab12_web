from django.db import models

# Create your models here.
class Book(models.Model): # database scheme
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)


class Address(models.Model):
    city = models.CharField(max_length = 50)
    def __str__(self):
        return self.city
    
class Student2(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

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

class company(models.Model):
     name = models.CharField(max_length=50)
     Address = models.TextField(max_length=50)

class product(models.Model):
     kind = models.CharField(max_length=50)
     company = models.ForeignKey(company, on_delete=models.CASCADE)
     expir_year = models.IntegerField()

class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student3(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)

class Document(models.Model):
    title = models.CharField(max_length=100)              
    file  = models.FileField(upload_to='documents/') 
