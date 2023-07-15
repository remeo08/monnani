from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from django.db.models import Count
from .serializers import ResultSerializer
from .models import Result


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
        all_answers = Result.objects.values("answer")
