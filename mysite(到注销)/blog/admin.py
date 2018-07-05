from django.contrib import admin

from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','author','body','publish')

admin.site.register(BlogArticles,BlogArticlesAdmin)
