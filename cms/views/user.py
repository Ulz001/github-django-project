from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from cms.serializers.UserSerializer import UserSerializer


class UserView(APIView):

    def get(self, request):
        return Response(status=HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors}, status=HTTP_400_BAD_REQUEST)
