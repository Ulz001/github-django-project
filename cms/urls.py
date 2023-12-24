from django.urls import re_path

from cms.views.login import LoginView
from cms.views.user import UserList, UserDetail

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('admin/', admin.site.urls),

    # re_path(r'^token/', obtain_jwt_token),

    re_path(r'^login/$', LoginView.as_view(), name='login'),
    # re_path(r'^login/$', obtain_jwt_token, name='login'),

    re_path(r'^users/$', UserList.as_view(), name='UserList'),
    re_path(r'^users/(?P<pk>[a-zA-Z0-9]+)/$', UserDetail.as_view(), name='UserDetail'),
]
