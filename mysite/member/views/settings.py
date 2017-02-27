from django.shortcuts import redirect, render
from django.views import View
from ..models import UserInfo

__all__ = [
    'UploadProfile',
    'UploadProfileContent',
]


class UploadProfile(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'member/settings/profile_picture.html', {})

    def post(self, request, *args, **kwargs):
        profile_img = request.FILES['profile_img']
        user_info = request.user.info
        user_info.profile_img = profile_img
        user_info.save()

        return redirect('member:personal_page')


class UploadProfileContent(View):

    def post(self, request, *args, **kwargs):
        dream = request.POST['dream']
        user_info = request.user.info
        user_info.dream = dream
        user_info.save()

        return redirect('member:personal_page')
