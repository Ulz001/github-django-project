from rest_framework.response import Response
from rest_framework.views import APIView

from cms.serializers.MaterialSerializer import MaterialSerializer
from cms.models import Material


class MaterialList(APIView):
    def get(self, request):
        materials = Material.objects.all()
        xAxisData = []
        seriesData = []
        serializer = MaterialSerializer(instance=materials, many=True)
        for material in serializer.data:
            material = dict(material)
            xAxisData.append(material["name"])
            seriesData.append(material["now_inventory"])
        return Response({"status": 200, "materials": [xAxisData, seriesData]})
