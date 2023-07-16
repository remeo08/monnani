from django.db import models


class Result(models.Model):
    result = models.CharField(max_length=30)
    mbti = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
