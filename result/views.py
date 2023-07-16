from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from django.db.models import Count
from .serializers import ResultSerializer, AnswerSerializer
from .models import Result
from collections import defaultdict


class Results(APIView):
    def get(self, request):
        all_results = Result.objects.all()
        serializer = ResultSerializer(all_results, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            new_result = serializer.save()
            return Response(
                ResultSerializer(new_result).data,
                status=HTTP_200_OK,
            )
        else:
            return Response(serializer.errors)


class TotalUser(APIView):
    def get(self, request):
        all_result = Result.objects.all().count()
        return Response(all_result)


class TopMBTI(APIView):
    def get(self, request):
        mbti_counts = (
            Result.objects.values("result")
            .annotate(count=Count("result"))
            .order_by("-count")
        )
        mbti_data = {mbti["result"]: mbti["count"] for mbti in mbti_counts}
        return Response(mbti_data)


class SelectedAnswers(APIView):
    def get(self, request):
        result = []
        all_answers = Result.objects.values("answer")
        serializer = AnswerSerializer(all_answers, many=True)

        counts = defaultdict(int)  # 중복 개수를 저장할 defaultdict 생성

        for item in serializer.data:
            answers = item["answer"].split(",")
            for answer in answers:
                counts[answer] += 1  # 각 문자열의 중복 개수 카운트

        result = [
            {"answer": answer, "count": count} for answer, count in counts.items()
        ]
        return Response(result)

        # result = []
        # all_answers = Result.objects.values("answer")
        # serializer = AnswerSerializer(all_answers, many=True)
        # for i in serializer.data:
        #     result.append(i["answer"].split(","))
        # return Response(result)
