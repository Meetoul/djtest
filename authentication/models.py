from django.db import models
from django.contrib.auth.models import User


class TestUser(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
