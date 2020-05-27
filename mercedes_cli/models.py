from django.db import models

from mercedes_cli.consts import UPLOAD_MBR_DIR
from mercedes_cli.lib import generate_gssn_reports


class CLIReport(models.Model):
    """
    Репортинг для штаб-квартиры Мерседес, делается раз в квартал
    """
    quarter = models.CharField('Квартал', max_length=2)
    rebus_data = models.FileField(
        'Данные Ребуса', max_length=200,
        help_text='Необходимо получить от индусов в виде excel с кодами вместо меток и удалить лишние строки шапки и лишние данные',
        upload_to=UPLOAD_MBR_DIR, null=True, blank=True
    )
    gssn_file = models.FileField(
        'GSSN коды ДЦ', max_length=250, help_text='Необходимо удалить лишние страницы', upload_to=UPLOAD_MBR_DIR,
        null=True, blank=True
    )
    cati_data_p1 = models.FileField(
        'RAW-data cati phase 1', max_length=250, upload_to=UPLOAD_MBR_DIR, null=True, blank=True
    )
    cati_data_p2 = models.FileField(
        'RAW-data cati phase 2-3', max_length=250, upload_to=UPLOAD_MBR_DIR, null=True, blank=True
    )
    cawi_data_p1 = models.FileField(
        'RAW-data cawi phase 1', max_length=250, upload_to=UPLOAD_MBR_DIR, null=True, blank=True
    )
    cawi_data_p2 = models.FileField(
        'RAW-data cawi phase 2-3', max_length=250, upload_to=UPLOAD_MBR_DIR, null=True, blank=True
    )
    report_p1 = models.FileField(
        'Репорт для штаб квартиры фаза 1', max_length=250, upload_to=UPLOAD_MBR_DIR, null=True, blank=True
    )
    report_p2 = models.FileField(
        'Репорт для штаб квартиры фазы 2-3', max_length=250, upload_to=UPLOAD_MBR_DIR, null=True, blank=True
    )
    state = models.TextField('Состояние генерации репорта', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.state = ''
        super().save()
        miss_fields = ', '.join([
            field.verbose_name for field in self._meta.get_fields()
            if field.name not in ('report_p1', 'report_p2', 'state', 'id') and not getattr(self, field.name)
        ])
        if miss_fields:
            self.state = 'Ожидается догрузка {files}'.format(files=miss_fields)
        else:
            generate_gssn_reports(self)
            self.state = 'Успешно завершено'
        super().save()

    def __str__(self):
        return self.quarter

    class Meta:
        verbose_name = 'Квартальный отчёт для Штаб-квартиры Мерседес Бенц'
        verbose_name_plural = 'Квартальные отчёты для Штаб-квартиры Мерседес Бенц'
