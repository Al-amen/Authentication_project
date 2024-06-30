from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_url = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
   
    def __str__(self):
        return self.user.username