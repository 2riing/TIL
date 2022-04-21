from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    # 팔로워
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')
    
    def get_rank(self):
        fan_count = self.fans.count()
        rank = 0
        if self.fans.count() > 100:
            rank = 1
        elif self.fans.count() >1000:
            rank = 2
        elif self.fans.count() >10000:
            rank = 3
        return rank
