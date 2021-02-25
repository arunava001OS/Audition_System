from django.db import models

from accounts.models import Profile

# Create your models here.
class Comment(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
