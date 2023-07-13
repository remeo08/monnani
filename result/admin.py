from django.contrib import admin
from .models import Result, Mbti, Answer


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "result",
        "created",
    )

@admin.register(Mbti)
class MbtiAdmin(admin.ModelAdmin):
    list_display = (
        "mbti",
        "created",
    )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "answer",
        "created",
    )
