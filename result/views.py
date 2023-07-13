from rest_framework.views import APIView
from rest_framework.response import Response
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
            )
        else:
            return Response(serializer.errors)

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