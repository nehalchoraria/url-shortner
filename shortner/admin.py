from django.contrib import admin
from .models import GeneratedLinks

class GeneratedLinksAdmin(admin.ModelAdmin):
    list_display = ('short_link','full_link') 

admin.site.register(GeneratedLinks, GeneratedLinksAdmin)