from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from cms.serializers.UserSerializer import UserSerializer


class RegisterView(APIView):

    def get(self, request):
        return Response(status=HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': HTTP_200_OK, 'data': serializer.data})
        else:
            return Response({'status': HTTP_400_BAD_REQUEST, 'errors': serializer.errors})
