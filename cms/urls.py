from django.urls import path

from cms.views.register import RegisterView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
]
