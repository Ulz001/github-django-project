from rest_framework_jwt.authentication import BaseAuthentication, BaseJSONWebTokenAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework import exceptions


# 未实现自定义认证类
class MyToken(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        # 拿到get请求在请求头中的AUTHORIZATION键对应的token值
        jwt_value = str(request.META.get('HTTP_AUTHORIZATION'))
        print(jwt_value)
        try:
            # 将token值的第二段转化成一个用户信息【没有密码】 还认证是否篡改，是否过期
            payload = jwt_decode_handler(jwt_value)
            print(payload)
        except Exception:
            raise exceptions.AuthenticationFailed("认证失败")
        # 根据payload得到用户对象
        user = self.authenticate_credentials(payload)
        print(user)  # admin 用户对象
        # 将用户对象返回
        return user, None
