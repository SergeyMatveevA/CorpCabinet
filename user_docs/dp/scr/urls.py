from django.conf.urls import url

from user_docs.dp import views

urlpatterns = [
    url(r'^config_survey_call_times', views.config_survey_call_times, name='config_survey_call_times'),
]
