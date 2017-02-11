from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.conf import settings
#
#
# class TaskUserManager(BaseUserManager):
#
#     def create_user(self, email, username, password):
#
#         user = self.model(email=email, username=username)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, username, password):
#
#         user = self.model(email=email, username=username)
#         user.set_password(password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user
#
#
# class TaskUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=50)
#     profile_img = models.ImageField()
#     level = models.IntegerField(default=1)
#     exp = models.FloatField(default=float(0))
#     last_login = models.DateTimeField(auto_now=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     REQUIRED_FIELDS = ['username']
#
#     USERNAME_FIELD = 'email'
#
#     object = TaskUserManager()
#
#     def __str__(self):
#         return self.username
#
#     def get_short_name(self):
#         return self.username
#
#     def get_full_name(self):
#         return self.username


class UserInfo(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='info')
    username = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    exp = models.FloatField(default=float(0))
    dream = models.TextField(blank=True)
    profile_img = models.ImageField(
        null=True,
        upload_to='profile/',
    )

    def __str__(self):
        return self.user.email
