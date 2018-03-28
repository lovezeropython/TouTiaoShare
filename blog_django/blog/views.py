from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import BlogArticle

def blog_title(request):
    blogs = BlogArticle.objects.all()

    return render(request,'blog/title.html',context=locals())

def blog_article(request,article_id):
    # article = BlogArticle.objects.get(id=article_id)
    article = get_object_or_404(BlogArticle,id=article_id)
    # get_object_or_404 第一个参数是类，第二个是 查询的参数

    return render(request,'blog/content.html',context=locals())

