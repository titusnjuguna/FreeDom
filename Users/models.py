from django.db import models
from django.contrib.auth.models import User ,AbstractUser



# Create your models here.
class User(AbstractUser):
    is_buyer = models.BooleanField(default= False)
    is_seller = models.BooleanField(default= False)

class buyer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username
    
class Seller(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username

    
"""class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prof_pic = models.ImageField(default='default.jpg',
        upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save()
        img = Image(self.prof_pic.path)
        if img.height > 300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.prof_pic.path)"""

        
