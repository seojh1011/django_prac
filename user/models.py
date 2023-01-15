from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=20)
    join_date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby = models.ManyToManyField("hobby")
    birthday = models.DateField()
    age = models.IntegerField()

class Hobby(models.Model):
    name = models.CharField(max_length=50)