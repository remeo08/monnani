from rest_framework.serializers import ModelSerializer
from .models import Result, Mbti, Answer


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        # fields = ("result","created",)
        fields = "__all__"


class MbtiSerializer(ModelSerializer):
    class Meta:
        model = Mbti
        # fields = ("result","created",)
        fields = "__all__"


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        # fields = ("result","created",)
        fields = "__all__"
