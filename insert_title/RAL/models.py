from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _




# Create your models here.
class ITUser(AbstractUser):
    
    ##  Taken from old project

    ## Added to enable the use of python manage.py createsuperuser with added required fields
    REQUIRED_FIELDS = ['username','firstname', 'lastname']
    USERNAME_FIELD = 'email'

    USERTYPES = (
        ('V','VISTOR'),
        ('A','ADMIN'),
        ('S','STUDENT'),
        ('R','RECRUITER'),
    )
    email=models.EmailField(max_length=250,unique=True)
    username = models.CharField(max_length=150 , unique=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    join_date = models.DateTimeField(auto_now_add=True)
    # Meaning?
    # is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    userType = models.CharField(max_length=256,choices=USERTYPES,default="V")
    
    #COMMON
    phone_number = models.TextField(null=True,blank=True)
    birthdate = models.DateTimeField(null=True,blank=True)
    bio = models.TextField(null=True,blank=True)

    #Student
    undergraduate_year = models.IntegerField(null=True,blank=True)
    university = models.TextField(null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    other_website_links = models.TextField(null=True, blank=True)

    #RECRUITER
    contact_links = models.TextField(null=True,blank=True)
    is_company = models.BooleanField(null=True,blank=True)
