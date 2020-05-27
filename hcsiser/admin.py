from django.contrib import admin

from arrangement.consts import ST_FIN, ST_ERR
from arrangement.lib import export_stratification
from hcsiser.models import Stratification, CSIRecalculate


class StratificationAdmin(admin.ModelAdmin):
    fields = [
        'numbers_of_complited', 'percentage_of_target', 'target', 'numbers_of_eliminated', 'numbers_of_fresh',
        'numbers_of_no_answered', 'numbers_of_appointments', 'description'
    ]
    list_display = [
        'numbers_of_complited', 'percentage_of_target', 'target', 'numbers_of_eliminated', 'numbers_of_fresh',
        'numbers_of_no_answered', 'numbers_of_appointments', 'description'
    ]
    empty_value_display = ''
    search_fields = ['field', 'field_val', 'description']
    list_filter = ['field', 'field_val', 'description', 'percentage_of_target']
    actions = [export_stratification]
    ordering = ['row_number']


class CSIRecalculateAdmin(admin.ModelAdmin):
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
admin.site.register(Stratification, StratificationAdmin)
