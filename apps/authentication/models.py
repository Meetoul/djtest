from django.db import models
from django.contrib.auth.models import User

from testing.models import Test


class TestUser(models.Model):
    user = models.OneToOneField(User)
    passed_tests = models.ManyToManyField(Test)

    def __str__(self):
        return self.user.username
