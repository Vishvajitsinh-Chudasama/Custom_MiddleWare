from django.contrib import admin

# Register your models here.

from .models import Requestlog

@admin.register(Requestlog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'method', 'path', 'status_code')
    list_filter = ('method', 'status_code')
    search_fields = ('path', 'error_message')