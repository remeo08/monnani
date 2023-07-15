from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShareSerializer
from django.db.models import Count
from .models import Share


class Shares(APIView):
    def get(self, request):
        all_share = Share.objects.all().count()
        shares_count = Share.objects.values("form_name").annotate(
            count=Count("form_name")
        )
        shared_data = {share["form_name"]: share["count"] for share in shares_count}
        return Response({"total_share": all_share, "shared_form": shared_data})

    def post(self, request):
        serializer = ShareSerializer(data=request.data)
        if serializer.is_valid():
            new_data = serializer.save()
            return Response(ShareSerializer(new_data).data)
        else:
            return Response(serializer.errors)
