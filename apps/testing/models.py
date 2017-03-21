from django.db import models
from django.utils import timezone


class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    result_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now)
    passes_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text[:20]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    correct = models.BooleanField()

    def __str(self):
        return self.text[:20]
