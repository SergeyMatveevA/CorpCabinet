from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from arrangement.consts import ST_FIN, ST_ERR
from hcsisal.models import CSIRecalculate


class CSIRecalculateAdmin(ImportExportModelAdmin):
    empty_value_display = ''
    list_display = [
        'create_date', 'original_file', 'processed_file', 'expiration_date', 'csi_index', 'processing_result',
        'processing_comments'
    ]

    def get_fields(self, request, obj=None):
        custom_fields = []
        if not obj:
            custom_fields = ['original_file']
        elif obj.processing_result == ST_FIN:
            custom_fields = [
                'create_date', 'original_file', 'processed_file', 'expiration_date', 'csi_index', 'processing_result'
            ]
        elif obj.processing_result == ST_ERR:
            custom_fields = ['create_date', 'original_file', 'processing_result', 'processing_comments']
        return custom_fields

    readonly_fields = ['create_date', 'processing_comments']


admin.site.register(CSIRecalculate, CSIRecalculateAdmin)