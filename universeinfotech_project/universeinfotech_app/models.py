from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.
class Banner_Slider(models.Model):
    title = models.CharField(max_length = 150) 
    image = models.ImageField(upload_to='Banner_slider', default='no.jpg')
    description  = models.TextField()

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    font_icon_code = models.CharField(max_length = 150) 
    description  = models.TextField()

    def __str__(self):
        return self.title

class Our_Service(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    font_icon_code = models.CharField(max_length = 150)  
    description  = models.TextField()

    def __str__(self):
        return self.title

class Project_Gallery(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    project_type = models.CharField(max_length = 50) 
    image = models.ImageField(upload_to='Project_Gallery', default='no.jpg')
    description  = models.TextField()

    def __str__(self):
        return self.title

class Developer_Profile(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    designation = models.CharField(max_length = 50) 
    image = models.ImageField(upload_to='Developer_Profile', default='no.jpg')
    facebook_link = models.URLField(max_length = 200, blank=True, null=True)
    twitter_link = models.URLField(max_length = 200, blank=True, null=True)
    dribbble_link = models.URLField(max_length = 200, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True, blank=True,null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='BlogImage', default='no.jpg')
    description =RichTextUploadingField('descriptions')
    
    def __str__(self):
        return self.title

class ClientsReview(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ClientsImg')
    review  = models.CharField(max_length = 250)
    rating  = models.FloatField()

    def __str__(self):
        return self.name

class Tools(models.Model):
    tilte = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ToolsImg')
    
    def __str__(self):
        return self.tilte
    

class Portfolio(models.Model):
    tilte = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ToolsImg')
    portfolio_link = models.URLField(max_length = 200)
    
    
    def __str__(self):
        return self.tilte
    