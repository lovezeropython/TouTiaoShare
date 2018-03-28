from django.contrib import admin

from .models import BlogArticle
# Register your models here.

# admin.site.register(BlogArticle)
@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish')
    raw_id_fields = ('author',)
    search_fields = ('title','author')
    date_hierarchy = "publish"
    # 过滤日期的方式是使用date_hierarchy选项
    ordering = ['publish','author']
