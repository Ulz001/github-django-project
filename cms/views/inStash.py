from rest_framework.response import Response
from rest_framework.views import APIView

from cms.serializers.InStashSerializer import InStashSerializer
from cms.models import InInventory


class InStashList(APIView):
    def get(self, request):
        data = InInventory.objects.all()
        xAxisData = []
        seriesData = []
        serializer = InStashSerializer(instance=data, many=True)
        for material in serializer.data:
            material = dict(material)
            xAxisData.append(material["material_name"])
            seriesData.append(material["num"])
        return Response({"status": 200, "InStashData": [xAxisData, seriesData]})
