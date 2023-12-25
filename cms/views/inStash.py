from rest_framework.response import Response
from rest_framework.views import APIView

from cms.serializers.InStashSerializer import InStashSerializer
from cms.models import InInventory, Material
from cms.serializers.MaterialSerializer import MaterialSerializer


class InStashList(APIView):
    def get(self, request):
        data = InInventory.objects.all()
        temp = {}
        res = []
        serializer = InStashSerializer(instance=data, many=True)
        for material in serializer.data:
            material = dict(material)
            material['material'] = MaterialSerializer(instance=Material.objects.get(pk=material["material"]), many=False).data['name']

            temp['name'] = material['material']
            temp['value'] = material['num']
            res.append(temp)
            temp = {}
        return Response({"status": 200, "InStashData": res})
