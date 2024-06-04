from django.core.management.base import BaseCommand
from www import models


# 自定制创建用户命令
class Command(BaseCommand):
    def handle(self, *args, **options):
        username = input("用户名：")
        password = input("密码：")
        models.User.objects.create(username=username, password=password, is_super=True)
        print("创建成功！")
