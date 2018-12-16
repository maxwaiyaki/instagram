from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'profile_pictures/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length = 150, blank=True)
    followers = models.ManyToManyField(User,related_name='followers', blank=True)

    def save_profile(self):
        self.save()

    def update_bio(self):
        self.bio = bio
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user

    @classmethod
    def search_user(cls, username):
        user = User.objects.get(username = username)
        return user


class Image(models.Model):
    
