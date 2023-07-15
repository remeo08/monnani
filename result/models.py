from django.db import models


class Result(models.Model):
    result = models.CharField(max_length=5)
    mbti = models.CharField(max_length=15)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
