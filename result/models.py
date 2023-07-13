from django.db import models
from common.models import CommonModel


class Result(CommonModel):
    
    """ INTJA mbti 그 자체만 받아옴 """

    result = models.CharField(
        max_length=5,
    )

    def __str__(self) -> str:
        return self.result


class Mbti(CommonModel):

    """ 선택지와 연결된 mbti """

    mbti = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.mbti


class Answer(CommonModel):

    """ 선택지 문자열 """

    answer = models.TextField()

    def __str__(self) -> str:
        return self.answer
