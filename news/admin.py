from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
  list_display=('title','news_desc')


admin.site.register(News,NewsAdmin)