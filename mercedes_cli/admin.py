from django.contrib import admin

from mercedes_cli.models import CLIReport


class CLIReportAdmin(admin.ModelAdmin):
    pass


admin.site.register(CLIReport, CLIReportAdmin)
