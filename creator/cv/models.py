from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.urls import reverse
from django.contrib.auth.models import User
import random
import datetime
def generateId(): 
    return random.randint(1, 50)*3




class resume_data(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    FullName = models.CharField(max_length=50)
    Profession = models.TextField()
    Profile = models.TextField(  )
    Address = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    University = models.TextField()
    Email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
  
    def __str__(self):
        return self.Email
    
class skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Skills = models.CharField( unique = True , max_length=50)

    def __str__(self):
        return self.Skills
    

class experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Heading = models.CharField(max_length=50)
    Post = models.TextField()
    From = models.DateField()
    To = models.DateField()
    Description = models.CharField( max_length=5000)

    def __str__(self):
        return self.Heading
    
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    School = models.CharField( max_length=50)
    Class = models.CharField(max_length=50)
    Cgpa = models.FloatField( )
    Passing_year = models.IntegerField( )

    def __str__(self):
        return self.School

    
