from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    status = [
        (1,'NOT_EVALUATED'),
        (2,'EVALUATED'),
        (3,'ELIMINATED'),
    ]

    user = models.OneToOneField(User,on_delete=CASCADE)
    curr_round = models.IntegerField(default=1)
    current_status = models.IntegerField(choices=status,default=1)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


