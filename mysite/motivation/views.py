from django.shortcuts import render
from django.views import View
from motivation.models import Post


class PostView(View):
    def get(self, request):
        context = {}
        post = Post.objects.order_by('?').first()
        context['post'] = post
        return render(request, 'motivation/posts.html', context)