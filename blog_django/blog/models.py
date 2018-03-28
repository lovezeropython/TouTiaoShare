from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogArticle(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(User, related_name='blog_posts')
    # User 和文章之间的关系是一对多的关系
    # related_name 允许 User 通过related_name 反向查询 文章
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        # 文章的排序 倒序，注意","
        ordering = ('-publish',)
        verbose_name = "博客文章"
        verbose_name_plural= "博客文章"

    def __str__(self):

        return self.title
