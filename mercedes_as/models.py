from datetime import datetime
from django.db import models

from arrangement.validators import xlsx_validate
from mercedes_as.conts import UPLOAD_MBR_DIR

ST_NEW = 'new'
ST_PROC = 'processing'
ST_ERR = 'error'
ST_FIN = 'final'
ST_NE_APP = 'need_approve'

PROCESSING_STATE = (
    (ST_NEW, 'Новая обработка'),
    (ST_PROC, 'В процессе обработки'),
    (ST_ERR, 'Ошибка обработки'),
    (ST_NE_APP, 'Необходимо подтвеждение первого этапа'),
    (ST_FIN, 'Обработка завершена')
)


class WaveBase(models.Model):
    """
    Класс для хранения оригинальных и обработаннных баз из смарт-даты по проекту AS
    """
    def_wave = '0{month}{year}'.format(month=str(datetime.now().month - 1), year=str(datetime.now().year))[-6:]

    wave = models.CharField(
        'Код волны', max_length=6, help_text='Код волны должен быть формата XX20YY, всегда 6 символов',
        default=def_wave
    )
    smartdata_base = models.FileField(
        'База из смартдаты', max_length=200, upload_to=UPLOAD_MBR_DIR, validators=[xlsx_validate],
        help_text='Заливается в формате xlsx'
    )
    state = models.CharField(
        'Статус обработки базы', max_length=45, default=ST_NEW, choices=PROCESSING_STATE, null=True
    )
    processed_base = models.FileField('Обработанная база смартдаты', max_length=200, null=True, blank=True)
    cawi_base = models.FileField('База для email-рассылки', max_length=200, null=True, blank=True)
    sms_base = models.FileField('База для sms-рассылки', max_length=200, null=True, blank=True)
    cati_base = models.FileField('База для cati-обзвона', max_length=200, null=True, blank=True)
    base_statisctic = models.FileField('Первичная статистика по обработке базы', max_length=200, null=True, blank=True)
    comments = models.CharField('Комментарии', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'База проекта Mercedes After Sales'
        verbose_name_plural = 'Базы проекта Mercedes After Sales'

    def __str__(self):
        return self.wave
