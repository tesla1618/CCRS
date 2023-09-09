from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class IUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    phone = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.user)

class Center(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,blank=True, null=True)
    phone = models.IntegerField(null=True,blank=True)
    cname = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to='static/center/dp/', default='static/center/dp/default.png')
    area = models.CharField(max_length=50,blank=True, null=True)
    halltype = models.CharField(max_length=50,blank=True, null=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    rent = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    isAvailable = models.BooleanField(default=True)
    fullAdd = models.TextField(null= True, blank= True)
    fbLink = models.CharField(max_length=1000, null= True, blank= True)
    igLink = models.CharField(max_length=1000, null= True, blank= True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cname)
        super(Center, self).save(*args, **kwargs)

    def __str__(self):
        return self.cname
    
class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null= True, blank= True)
    center = models.OneToOneField(Center, on_delete=models.CASCADE,null= True, blank= True)
    
    date = models.CharField(max_length=100, null= True, blank= True)
    cost = models.IntegerField(null= True, blank= True)
    eventType = models.CharField(max_length=500, null= True, blank= True)
    trxid = models.CharField(max_length=500, null= True, blank= True)

    # def __str__(self):
    #     return self.user + " booked " + self.center
    