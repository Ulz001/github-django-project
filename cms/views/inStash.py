from rest_framework.response import Response
from rest_framework.views import APIView

from cms.serializers.InStashSerializer import InStashSerializer
from cms.models import InInventory
from cms.utils.method import handling_data


class InStashList(APIView):
    def get(self, request):
        data = InInventory.objects.all()
        serializer = InStashSerializer(instance=data, many=True)
        res = handling_data(serializer.data)
        return Response({"status": 200, "data": res})
