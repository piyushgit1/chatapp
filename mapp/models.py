from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    location = models.CharField(max_length=30, default="Home", blank=True)
    mobile_number = models.BigIntegerField(blank=False, unique=True)
    avtar = models.ImageField(upload_to='ProfilePic/', blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.mobile_number


class Contacts(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="account", related_query_name="usercontact")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='ProfilePic/', blank=True)
    mobile_number = models.BigIntegerField()

    class Meta:
        ordering = ('first_name',)


class Messages(models.Model):
      contact=models.ManyToManyField(Contacts)
      user=models.CharField(max_length=100)
      message=models.TextField()