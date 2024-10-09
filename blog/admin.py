from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'released_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, PostAdmin)
