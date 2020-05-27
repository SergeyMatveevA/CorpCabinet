from django.conf.urls import url

from user_docs.fw import views

urlpatterns = [
    url(r'^huindai_finish_control$', views.huindai_finish_control, name='huindai_finish_control'),
    url(r'^make_appointment$', views.make_appointment, name='make_appointment'),
    url(r'^make_appointment_range$', views.make_appointment_range, name='make_appointment_range'),
    url(r'^paste_to_excel$', views.paste_to_excel, name='paste_to_excel'),
]
