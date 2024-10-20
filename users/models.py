from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    profile_picture = models.ImageField('Avatar', upload_to='users/avatars', null=True, blank=True)
    role = models.CharField('Role', max_length=10, default='user')
    is_blocked = models.BooleanField('Is blocked', default=False)
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.id} -  {self.username}'
