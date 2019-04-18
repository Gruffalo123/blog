from django.contrib import admin

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','public_time')
    list_filter = ('public_time',)

    
admin.site.register(Article,ArticleAdmin)
