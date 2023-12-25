from rest_framework.views import APIView
from rest_framework.response import Response

from cms.serializers.OutStashSerializer import OutStashSerializer, OutInventory
from cms.utils.method import handling_data


class OutStashList(APIView):
    def get(self, request):
        out_stash_data = OutInventory.objects.all()
        serializer = OutStashSerializer(out_stash_data, many=True)
        result = handling_data(serializer.data)
        return Response({"status": 200, "data": result})
