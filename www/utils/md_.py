from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class AuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # if request.path_info in ["/login/"]:
        if request.path_info in [reverse("login")]:
            return

        user_dict = request.session.get("userinfo")
        if not user_dict:
            return redirect('login')
        # 用户已经登录，将用户信息封装在request中
        request.user_dict = user_dict

class PermissionMiddleware(MiddlewareMixin):
    def process_view(self,request,callback,*args,**kwargs):
        if request.path_info in [reverse("login")]:
            return

        # 判断是否是超级用户
        if request.user_dict["isSuper"]:
            return

        pass

        # url_name = request.resolver_match.url_name