from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from .serializers import ResultSerializer, AnswerSerializer, MbtiSerializer
from .models import Result, Mbti, Answer


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


class ResultsDetail(APIView):
    def get_object(self, pk):
        try:
            one_result = Result.objects.get(pk=pk)
        except Result.DoesNotExist:
            raise NotFound
        return one_result

    def get(self, request, pk):
        serializer = ResultSerializer(self.get_object(pk))
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class TopResult(APIView):
    pass
    # def get(request):
    #     result = Result.objects.all()
    #     mbti_list = []
    #     mbti_count_list = {}
    #     for i in mbti_list:
    #         mbti_count = Result.objects.filter(mbti=i).count()
    #         mbti_count_list[i] = mbti_count

    #     return


class Answers(APIView):
    def get(self, request):
        all_answers = Answer.objects.all()
        serializer = AnswerSerializer(all_answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            new_answer = serializer.save()
            return Response(
                AnswerSerializer(new_answer).data,
                status=HTTP_200_OK,
            )
        else:
            return Response(serializer.errors)


class AnswersDetail(APIView):
    def get_object(self, pk):
        try:
            one_answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise NotFound
        return one_answer

    def get(self, request, pk):
        serializer = AnswerSerializer(self.get_object(pk))
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Mbtis(APIView):
    def get(self, request):
        all_mbtis = Mbti.objects.all()
        serializer = MbtiSerializer(all_mbtis, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MbtiSerializer(data=request.data)
        if serializer.is_valid():
            new_mbti = serializer.save()
            return Response(
                MbtiSerializer(new_mbti).data,
                status=HTTP_200_OK,
            )
        else:
            return Response(serializer.errors)


class MbtisDetail(APIView):
    def get_object(self, pk):
        try:
            one_mbti = Mbti.objects.get(pk=pk)
        except Mbti.DoesNotExist:
            raise NotFound
        return one_mbti

    def get(self, request, pk):
        serializer = MbtiSerializer(self.get_object(pk))
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
