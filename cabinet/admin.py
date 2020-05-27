from django.contrib import admin

from cabinet.models import ResponseCode


class ResponseCodeAdmin(admin.ModelAdmin):
    fields = ['code', 'label', 'survey']
    list_display = ['code', 'label', 'survey']
    list_filter = ['code', 'label', 'survey']
    search_fields = ['code', 'label', 'survey']


admin.site.register(ResponseCode, ResponseCodeAdmin)
