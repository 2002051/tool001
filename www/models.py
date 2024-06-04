from django.db import models

# Create your models here.


from django.db import models


class Permission(models.Model):
    """ 权限表 """
    code = models.CharField(verbose_name="路由名称", max_length=32)
    name = models.CharField(verbose_name="名称", max_length=32)

    def __str__(self):
        return self.name


class Role(models.Model):
    """ 角色表 """
    name = models.CharField(verbose_name="角色", max_length=32)

    permissions = models.ManyToManyField(verbose_name="权限", to="Permission")

    def __str__(self):
        return self.name


class Menu(models.Model):
    """ 菜单 """
    title = models.CharField(verbose_name="菜单", max_length=32)
    permissions = models.ManyToManyField(verbose_name="权限", to="Permission")

    def __str__(self):
        return self.title


class User(models.Model):
    """ 用户表 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    is_super = models.BooleanField(verbose_name="是否超级用户", default=False)

    roles = models.ManyToManyField(verbose_name="角色", to="Role", blank=True)
    menus = models.ManyToManyField(verbose_name="菜单", to="Menu", blank=True)


class Computer(models.Model):
    """ 电脑 """
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")


class Order(models.Model):
    """ 订单 """
    title = models.CharField(verbose_name="订单号", max_length=32)
    price = models.IntegerField(verbose_name="价格")