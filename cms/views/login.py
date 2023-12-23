from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework.views import APIView


class LoginView(APIView):
    def post(self, request):
        user = User.objects.get(username=request.data["username"])
        if user.check_password(request.data["password"]):
            return Response({'status': 200, 'token': "token"})
        else:
            return Response({'status': 401, 'error': '密码错误'})
