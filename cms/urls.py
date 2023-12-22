from django.urls import path

from cms.views.user import UserView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/users/', UserView.as_view(), name='user'),
]
