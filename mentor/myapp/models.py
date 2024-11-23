from django.db import models

# Create your models here.
class Trainers(models.Model):
    name=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    about=models.TextField()
    picture=models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.name} {self.profession}"
    
class About(models.Model):
    name=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    feedback=models.TextField()
    picture=models.ImageField(upload_to='images/')
    def __str__(self):
        return f"{self.name} {self.profession}"   
    
class Courses(models.Model):
    t_name=models.CharField(max_length=100)
    c_name=models.CharField(max_length=100)
    c_heading=models.CharField(max_length=100)
    about=models.TextField()
    c_pic=models.ImageField(upload_to='images/')
    t_pic=models.ImageField(upload_to='images/')
    price=models.DecimalField(max_digits=10, decimal_places=5)
    def __str__(self):
        return f"{self.c_name}"       

class Customar(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()    
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return f"{self.name}"
    
