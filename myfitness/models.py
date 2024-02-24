from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField('auth.Group', related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_user_permissions', blank=True)


class Fitness(models.Model):
    
    class Meta:
        unique_together = (('user_name', 'date', 'lift'),)
        
    user_name = models.CharField(max_length=50)
    date = models.DateField(default= date.today().strftime('%d-%m-%Y'))
    lift = models.CharField(max_length=50)
    reps = models.IntegerField(max_length=3)
    weight = models.IntegerField(max_length=3)


class Calorie(models.Model):
    
    class Meta:
        unique_together = (('user_name', 'type'),)
        
    user_name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    calorie = models.IntegerField(max_length=3)
    protein = models.IntegerField(max_length=3)
    carbs = models.IntegerField(max_length=3)
    fats = models.IntegerField(max_length=3)