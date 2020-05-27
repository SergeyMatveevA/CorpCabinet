from django.db import models


class ResponseCode(models.Model):
    """
    Респоонс-коды нипы
    """
    code = models.IntegerField('Код')
    label = models.CharField('Название респонса', max_length=120)
    survey = models.CharField('Проект', max_length=7, default='default')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Респонс код'
        verbose_name_plural = 'Респонс коды'
        unique_together = (('code', 'survey'),)
