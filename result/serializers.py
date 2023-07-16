from rest_framework.serializers import ModelSerializer
from .models import Result


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = ("answer",)
