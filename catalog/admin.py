from django.contrib import admin

from .models import Mark, ModelAuto


class AutoModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Mark, AutoModelAdmin)
admin.site.register(ModelAuto)
