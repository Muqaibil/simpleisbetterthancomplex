from django.contrib import admin

# Register your models here.
from .models import Post

class postAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish_date', 'view_count']
    list_filter = ['publish_date']
    search_fields = ['title', 'content']
    date_hierarchy = 'publish_date'

admin.site.register(Post, postAdmin)
