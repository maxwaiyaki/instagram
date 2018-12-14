from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'profile_pictures/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length = 100, blank=True)
    followers = ManyToManyField(User,related_name='followers', blank=True)
