import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sv.settings')

app = Celery('sv')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'rtk_compls' : {
        'task': 'sv.tasks.rtk_complaints',
        'schedule': crontab(),
    },
    'stratification_update': {
        'task': 'sv.tasks.stratification_reload',
        'schedule': crontab('*/15'),
    },
    'check_new_surveys': {
        'task': 'sv.tasks.surveys_check',
        'schedule': crontab('*/15'),
    },
    'update_survey_names': {
        'task': 'sv.tasks.update_survey_names',
        'schedule': crontab('*/15'),
    },
    'change_sample_activity': {
        'task': 'sv.tasks.change_sample_activity',
        'schedule': crontab(),
    },
    'rtk_audio_upload': {
        'task': 'sv.tasks.add_rtk_audio',
        'schedule': crontab(),
    },
    'handle_generation_short_links': {
        'task': 'sv.tasks.handle_yourls_generations',
        'schedule': crontab(),
    }
}
