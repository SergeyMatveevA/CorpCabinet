from datetime import datetime, timedelta

from django.db import models

from arrangement.consts import ST_NEW, PROCESSING_STATE
from arrangement.validators import xlsx_validate
from f2ffield.consts import UPLOAD_DIR
from f2ffield.lib import calculate_interviews


class InterviewsCalculate(models.Model):
    survey_name = models.CharField('Название проекта', max_length=55, help_text='Не обязательно', blank=True, null=True)
    quotas_file = models.FileField(
        'Файл с квотами', max_length=250, validators=[xlsx_validate], help_text='Файлы только в формате xlsx',
        upload_to=UPLOAD_DIR
    )
    state = models.CharField('Состояние обработки файла', max_length=25, default=ST_NEW, choices=PROCESSING_STATE)
    expiration_date = models.DateField('Дата удаления', null=True, blank=True)

    class Meta:
        verbose_name = 'Рассчёт количества интервью на интервьюера'
        verbose_name_plural = 'Рассчёт количества интервью на интервьюера'

    def save(self, *args, **kwargs):
        self.expiration_date = datetime.now() + timedelta(days=7)
        if self.state == ST_NEW:
            super().save()
            calculate_interviews(self)
        super().save()

    def __str__(self):
        return str(self.quotas_file).split('/')[-1]
