from django.contrib import admin

from arrangement.lib import export_xlsx
from yourls.models import YourlsUrl, Yourls2Url, YourlsLog, Yourls2Log


class YourlsUrlAdmin(admin.ModelAdmin):
    fields = ['keyword', 'url', 'title', 'timestamp', 'clicks']
    list_display = ['keyword', 'short_link', 'url', 'title', 'timestamp', 'clicks']
    readonly_fields = ['timestamp', 'clicks']
    search_fields = ['keyword']
    actions = [export_xlsx]


class YourlsLogAdmin(admin.ModelAdmin):
    fields = ('click_time', 'referrer', 'user_agent', 'ip_address', 'country_code')
    list_display = ('shorturl', 'click_time', 'referrer', 'user_agent', 'ip_address', 'country_code')
    readonly_fields = ('shorturl', 'click_time', 'referrer', 'user_agent', 'ip_address', 'country_code')


class Yourls2LogAdmin(admin.ModelAdmin):
    fields = ('click_time', 'referrer', 'user_agent', 'ip_address', 'country_code')
    list_display = ('shorturl', 'click_time', 'referrer', 'user_agent', 'ip_address', 'country_code')
    readonly_fields = ('shorturl', 'click_time', 'referrer', 'user_agent', 'ip_address', 'country_code')


class Yourls2UrlAdmin(admin.ModelAdmin):
    fields = ['keyword', 'url', 'title', 'timestamp', 'clicks']
    list_display = ['keyword', 'short_link', 'url', 'title', 'timestamp', 'clicks']
    readonly_fields = ['timestamp', 'clicks', 'short_link']
    search_fields = ['keyword']
    actions = [export_xlsx]


admin.site.register(YourlsUrl, YourlsUrlAdmin)
admin.site.register(Yourls2Url, Yourls2UrlAdmin)
admin.site.register(YourlsLog, YourlsLogAdmin)
admin.site.register(Yourls2Log, Yourls2LogAdmin)
