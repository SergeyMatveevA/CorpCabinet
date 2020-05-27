from django.conf.urls import url

from cabinet import views

urlpatterns = [
    url(r'^dialing_sample$', views.dialing_sample, name='dialing_sample'),
    url(r'^dialing_contact_log$', views.dialing_contact_log, name='dialing_contact_log'),
    url(r'^help$', views.help, name='help'),
    url(r'^stratification$', views.stratification, name='stratification'),
    url(r'^fieldwork_control$', views.fieldwork_control, name='fieldwork_control'),
]
