
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
publish_choice = [
    ('0',"draft"),
    ('1',"publish"),
    ('2',"archrive"),
]
    
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)    
    desc = models.TextField(null=True ,blank=True)
    img = models.ImageField(upload_to = 'img', default='default.img')
    publish = models.CharField(choices= publish_choice ,max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
