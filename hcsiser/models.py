from datetime import datetime, timedelta
from django.db import models

from arrangement.consts import PROCESSING_STATE, ST_NEW
from arrangement.validators import xlsx_validate
from hcsiser.consts import UPLOAD_DIR
from hcsiser.lib import csi_recalculate


class Stratification(models.Model):
    """
    Стандартная стратификация проекта
    """
    row_number = models.IntegerField('Номер строки в файле стратифкации', primary_key=True)
    field = models.CharField('Поле в БД', max_length=250)
    field_val = models.CharField('Значение поля в БД', max_length=250)
    target = models.IntegerField('Размер квоты')
    description = models.CharField('Описание квоты', max_length=250, null=True)
    numbers_of_complited = models.IntegerField('Количество успешных', default=0)
    numbers_of_fresh = models.IntegerField('Количество свежих контактов', default=0)
    numbers_of_appointments = models.IntegerField('Количество договоренностей', default=0)
    numbers_of_no_answered = models.IntegerField('Количество не ответивших', default=0)
    numbers_of_eliminated = models.IntegerField('Количество использованных', default=0)
    percentage_of_target = models.CharField('Процент выполнения квоты', max_length=10, default="0%")

    def __str__(self):
        if self.description:
            return self.description
        else:
            '%s %s'.format(self.field, self.field_val)

    class Meta:
        verbose_name = 'Строка стратифкации'
        verbose_name_plural = 'Стратифкация Хёндай сервис 2019'


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
