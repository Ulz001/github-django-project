from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings


class LoginView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        user = User.objects.get(username=request.data["username"])
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        if user.check_password(request.data["password"]):
            return Response({'status': 200, 'token': token})
        else:
            return Response({'status': 401, 'error': '密码错误'})
