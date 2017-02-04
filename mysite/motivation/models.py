from django.db import models


class Post(models.Model):
    # 일단은 글로만 생각하고 있습니다.
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=300)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text[:40])
