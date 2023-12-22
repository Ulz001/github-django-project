from django.http import JsonResponse

from django.views import View


class RegisterView(View):
    def get(self):
        ...

    def post(self, request):
        return JsonResponse({'status': 'ok'})
