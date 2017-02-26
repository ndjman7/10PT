from motivation.models import Post

def random_post(request):
    post = Post.objects.order_by('?').first()
    return {'post': post}