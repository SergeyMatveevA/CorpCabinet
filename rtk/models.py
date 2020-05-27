from datetime import datetime as dt

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from rtk.consts import TOUCH_POINTS, RTK_REGIONS, COMPL_PROCESSING, COMPL_RESULT, STATE, AUDIO_UPLOAD_RTK


class Complaint(models.Model):
    id = models.AutoField('Номер ТТ', primary_key=True)
    telephone = models.CharField('Телефон', max_length=11)
    abonent_id = models.CharField('ID абонента', max_length=30)
    translate_reason = models.CharField('Причина перевода', choices=COMPL_PROCESSING, max_length=25)
    translate_result = models.CharField('Результат перевода', choices=COMPL_RESULT, max_length=25, blank=True, null=True)
    translate_result_other = models.TextField('Результат перевода другое', blank=True, null=True)
    appointment_time = models.DateTimeField('Желаемое время/дата перезвона', blank=True, null=True)
    appointment_comment = models.TextField('Комментарий к перезвону', null=True, blank=True)
    processed_comment = models.TextField('Комментарий к обработке', null=True, blank=True)
    ready_recommend = models.IntegerField('Готовность рекомендовать',  validators=[
        MinValueValidator(0), MaxValueValidator(10)
    ])
    negative_reason_rtk = models.TextField('Причина низкой оценки')
    cc_satisfaction = models.IntegerField('Удовлетворенность работой',  validators=[
        MinValueValidator(0), MaxValueValidator(5)
    ])
    negative_reason_cc = models.TextField('Причина низкой оценки работы call-центра')
    state_compl = models.CharField('Статус ТТ', choices=STATE, max_length=25, default='preparing')
    creation_date = models.DateTimeField('Дата создания')
    change_date = models.DateTimeField('Дата изменения', null=True, blank=True)
    survey_name = models.CharField('Имя проекта в нипо', max_length=7)
    interview_number = models.IntegerField('Номер интервью в нипо')
    region = models.CharField('Макрорегиональный филиал', max_length=1, choices=RTK_REGIONS, null=True, blank=True)
    touch_point = models.IntegerField('Точка контакта', choices=TOUCH_POINTS, null=True, blank=True)
    city_quota = models.IntegerField('Поле City_QUOTA из нипы', null=True)
    audio = models.FileField('Аудиозапись', max_length=250, upload_to=AUDIO_UPLOAD_RTK, blank=True, null=True)
    region_name = models.CharField('Регион из нипо', max_length=150, null=True, blank=True)

    def __str__(self):
        return '№{id}'.format(id=self.id)

    def save(self, *args, **kwargs):
        if self.state_compl != 'new':
            self.change_date = dt.now()
        super(Complaint, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заявка абонента о проблеме'
        verbose_name_plural = 'Заявки абонента о проблеме'
