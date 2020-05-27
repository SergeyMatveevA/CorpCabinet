from datetime import datetime, timedelta
from django.db import models

from arrangement.consts import PROCESSING_STATE, ST_NEW
from arrangement.validators import xlsx_validate
from hcsisal.consts import UPLOAD_DIR
from hcsisal.lib import csi_recalculate


class CSIRecalculate(models.Model):
    original_file = models.FileField(
        'Файл для обработки', help_text='Файлы принимаются только в формате .xlsx',
        validators=[xlsx_validate], upload_to=UPLOAD_DIR, max_length=300
    )
    processed_file = models.FileField(
        'Обработанный файл', null=True, blank=True, max_length=300, upload_to=UPLOAD_DIR
    )
    create_date = models.DateTimeField('Дата сохранения', auto_now=True)
    expiration_date = models.DateField('Дата удаления', null=True, blank=True)
    csi_index = models.FloatField('CSI индекс базы', null=True, blank=True)
    processing_result = models.CharField(
        'Результат обработки', choices=PROCESSING_STATE, max_length=20,
        help_text="Для повторной обработки необходимо указать 'Новая обработка'", default=ST_NEW
    )
    processing_comments = models.TextField('Комментарии по обработке')

    class Meta:
        verbose_name = 'Перерассчитанный CSI-индекс'
        verbose_name_plural = 'Перерассчёт CSI-индекса'

    def save(self, *args, **kwargs):
        self.expiration_date = datetime.now() + timedelta(days=7)
        if self.processing_result == ST_NEW:
            super().save()
            csi_recalculate(self)
        super().save()

    def __str__(self):
        return str(self.original_file).split('/')[-1]
