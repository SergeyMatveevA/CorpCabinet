from django.contrib import admin

from mercedes_as.models import WaveBase


class WaveBaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(WaveBase, WaveBaseAdmin)
