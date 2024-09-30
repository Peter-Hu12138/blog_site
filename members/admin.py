from django.contrib import admin
from . import models

class MembersAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "joined_date", 'age']

# Register your models here.
admin.site.register(models.Member, MembersAdmin)