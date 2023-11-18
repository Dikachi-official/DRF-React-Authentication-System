from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



# PROFILE MODEL
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

# USING SIGNALS TO AUTO SAVE THE CREATED USER PROFILE ABOVE
def create_user_profile(sender, instance, created, **kwargs):
    # refering to the created argument above
    if created:
        Profile.objects.create(user=instance)  # instance of User class

# Func to save
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Connects d created profile instance of User
post_save.connect(create_user_profile, sender=User)

# Saves the connected new user
post_save.connect(save_user_profile, sender=User)