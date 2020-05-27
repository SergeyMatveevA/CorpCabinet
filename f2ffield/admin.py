from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from arrangement.consts import ST_FIN
from f2ffield.models import InterviewsCalculate


class InterviewsCalculateAdmin(ImportExportModelAdmin):
    empty_value_display = ''
    list_display = ['pk', 'survey_name', 'quotas_file', 'state', 'expiration_date']
    search_fields = ['survey_name', 'quotas_file']
    list_filter = ['survey_name', 'state', 'expiration_date']

    def get_fields(self, request, obj=None):
        custom_fields = []
        if not obj:
            custom_fields = ['survey_name', 'quotas_file']
        elif obj.state == ST_FIN:
            custom_fields = ['survey_name', 'quotas_file', 'state', 'expiration_date']
        return custom_fields
    readonly_fields = ['state']


admin.site.register(InterviewsCalculate, InterviewsCalculateAdmin)
