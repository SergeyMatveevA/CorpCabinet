from django.contrib import admin
from django.shortcuts import redirect

from arrangement.lib import export_xlsx, send_mail
from arrangement.models import Survey, StandardTasks, ActiveJobs, Feedback


class SurveyAdmin(admin.ModelAdmin):
    fields = [
        'name', 'cati_programm_name', 'server_name', 'last_sample_activity', 'stratification',
        'stratification_update_date'
    ]
    list_display = ['cati_programm_name', 'name', 'server_name', 'last_sample_activity', 'stratification_update_date']


class StandardTasksAdmin(admin.ModelAdmin):
    fields = ['name', 'readable_name', 'state']
    list_display = ['readable_name', 'state']


class ActiveJobsAdmin(admin.ModelAdmin):
    fields = ['survey', 'task', 'state', 'expiration_date']
    list_display = ['survey', 'task', 'state', 'expiration_date']
    actions = [export_xlsx]


class FeedbackAdmin(admin.ModelAdmin):
    fields = ['content']
    list_display = ['author']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.author = request.user
        super().save_model(request, obj, form, change)
        m_text = '<br>Добавлен отзыв,<br>{content}'.format(content=obj.content)
        send_mail(
            ['Sergey.Matveev@ipsos.com', 'Svetlana.Doilneva@ipsos.com', 'Sergey.Zakharov@ipsos.com',
             request.user.email], m_text, 'Обратная связь №{id}'.format(id=obj.pk)
        )

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/admin/')

    change_form_template = "arrangement/one_button.html"

    def response_change(self, request, obj):
        return super().response_change(request, obj)


admin.site.register(Survey, SurveyAdmin)
admin.site.register(StandardTasks, StandardTasksAdmin)
admin.site.register(ActiveJobs, ActiveJobsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
