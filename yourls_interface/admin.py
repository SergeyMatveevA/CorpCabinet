from django.contrib import admin

from arrangement.consts import ST_FIN, ST_ERR, ST_NEW
from yourls_interface.models import YourlsID, LinkGeneration


class YourlsIDAdmin(admin.ModelAdmin):
    list_display = ['yourls_id', 'use_in_general_engine', 'use_in_mbr_engine', 'id_type']
    fields = ['yourls_id', 'use_in_general_engine', 'use_in_mbr_engine', 'id_type']
    list_filter = ['use_in_general_engine', 'use_in_mbr_engine', 'id_type']
    search_fields = ['yourls_id']


class LinkGenerationAdmin(admin.ModelAdmin):
    list_display = ['survey_name', 'links_file', 'engine', 'self_id', 'expiration_date', 'state']
    list_filter = ['engine', 'survey_name', 'title', 'self_id', 'expiration_date', 'state']
    search_fields = ['links_file', 'survey_name', 'title']

    def get_fields(self, request, obj=None):
        custom_fields = []
        if not obj or obj.state == ST_NEW:
            custom_fields = ['links_file', 'engine', 'survey_name', 'title', 'self_id']
        elif obj.state == ST_FIN:
            custom_fields = ['links_file', 'engine', 'survey_name', 'title', 'self_id', 'state', 'expiration_date']
        elif obj.state == ST_ERR:
            custom_fields = ['links_file', 'engine', 'survey_name', 'title', 'self_id', 'state', 'processed_comments']
        return custom_fields

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        if obj and obj.state == ST_FIN:
            readonly_fields = ['links_file', 'engine', 'survey_name', 'title', 'self_id', 'expiration_date', 'state']
        elif obj and obj.state == ST_ERR:
            readonly_fields = ['processed_comments']
        return readonly_fields


admin.site.register(YourlsID, YourlsIDAdmin)
admin.site.register(LinkGeneration, LinkGenerationAdmin)
