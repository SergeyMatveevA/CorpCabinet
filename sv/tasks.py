from celery import Celery

from arrangement.consts import ST_NEW
from arrangement.models import Survey
from arrangement.lib import check_new_surveys, update_sample_activity, fill_survey_names
from rtk.lib import complaint_translate, audio_upload
from yourls_interface.lib import generate_short_links
from yourls_interface.models import LinkGeneration

app = Celery('tasks', broker='pyamqp://admin@localhost/myvhost/')
app.config_from_object('django.conf:settings')


@app.task
def rtk_complaints():
    complaint_translate()


@app.task
def stratification_reload():
    for survey in Survey.objects.all():
        survey.stratification_update()

@app.task
def surveys_check():
    check_new_surveys()


@app.task
def add_rtk_audio():
    audio_upload()

@app.task
def handle_yourls_generations():
    for gen in LinkGeneration.objects.filter(state=ST_NEW):
        generate_short_links(gen)


@app.task
def change_sample_activity():
    update_sample_activity()


@app.task
def update_survey_names():
    fill_survey_names()
