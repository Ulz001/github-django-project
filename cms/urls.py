from django.urls import re_path

from cms.views.check import CheckList
from cms.views.inStash import InStashList
from cms.views.login import LoginView
from cms.views.outStash import OutStashList
from cms.views.register import RegisterView
from cms.views.user import UserList, UserDetail
from cms.views.material import MaterialList

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('admin/', admin.site.urls),

    # re_path(r'^token/', obtain_jwt_token),

    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    # re_path(r'^login/$', obtain_jwt_token, name='login'),

    re_path(r'^users/$', UserList.as_view(), name='UserList'),
    re_path(r'^users/(?P<pk>[a-zA-Z0-9]+)/$', UserDetail.as_view(), name='UserDetail'),

    re_path(r'^materials/$', MaterialList.as_view(), name='MaterialList'),

    re_path(r'^in-stash/$', InStashList.as_view(), name='InStashList'),

    re_path(r'^out-stash/$', OutStashList.as_view(), name='OutStashList'),
]
