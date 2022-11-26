from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key = True)
    pass

class List(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50, unique = True)
    description = models.TextField(default = '', unique = True)
    startbid = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.ImageField(upload_to = 'List/', blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name ="Lististuser")
    active = models.BooleanField(default = 'False')
    close = models.BooleanField(default = 'False')

    def __str__(self):
        return f'{self.title} price: {self.startbid}'

class Bid(models.Model):
    id = models.AutoField(primary_key = True)
    lists = models.ForeignKey(List, on_delete = models.CASCADE, related_name = "list")
    participant = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "participant")
    bid = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    selected = models.BooleanField(default = "False")
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return f'{self.participant} placed ({self.bid}) in {self.lists}'

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "commentname")
    comments = models.ForeignKey(List, on_delete = models.CASCADE, related_name = "comment")
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return f'{self.name} commented ({self.comment}) in {self.comments}'

class Category(models.Model):
    category = models.CharField(max_length = 100,unique = True)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return f"{self.category}"
