from datetime import datetime, timedelta
from django.db import models

from arrangement.consts import PROCESSING_STATE, ST_NEW
from arrangement.validators import xlsx_validate
from yourls_interface.consts import UPLOAD_DIR, ENGINES, GENERAL_ENGINE


class LinkGeneration(models.Model):
    """Создание ссылок в движке коротких ссылок"""
    links_file = models.FileField(
        'Файл ссылок', max_length=150, upload_to=UPLOAD_DIR, validators=[xlsx_validate],
        help_text='Файлы загружаются в формате xlsx, колонка содержащая ссылки должна иметь имя "link"'
    )
    engine = models.CharField(
        'Имя хоста', max_length=15, choices=ENGINES, default=GENERAL_ENGINE,
        help_text='Движок ANONYMOUS.ru используется только для проектов ANONYMOUS'
    )
    survey_name = models.CharField('Проект', max_length=150)
    title = models.CharField(
        'Заголовок страницы', max_length=200,
        help_text='Данный параметр определяет текст отображаемый в предзагрузке страницы - например в мессенджерах или '
                  'sms-приложениях'
    )
    self_id = models.BooleanField(
        'Использовать id из файла', default=False,
        help_text='Для использования id из файла, в файле должна быть колонка помеченная именем "id"'
    )
    expiration_date = models.DateField('Дата удаления', null=True, blank=True)
    state = models.CharField('Состояние генерации', choices=PROCESSING_STATE, default=ST_NEW, max_length=25)
    processed_comments = models.CharField('Комментарии по генерации', max_length=250, null=True)

    class Meta:
        verbose_name = 'Файл для генерации коротких ссылок'
        verbose_name_plural = 'Генерация коротких ссылок'

    def __str__(self):
        return str(self.links_file).split('/')[-1]

    def save(self, *args, **kwargs):
        self.expiration_date = datetime.now() + timedelta(days=7)
        super().save()


class YourlsID(models.Model):
    """Id для кейвордов движка коротких ссылок Yourls"""
    ID_TYPES = (
        (1, 'system'),
        (2, 'custom'),
    )

    yourls_id = models.CharField('Id в системе Yourls', max_length=50, primary_key=True)
    use_in_general_engine = models.BooleanField('Использовано для общего движка', default=False)
    use_in_mbr_engine = models.BooleanField('Использовано для движка ANONYMOUS', default=False)
    id_type = models.IntegerField('Тип id', choices=ID_TYPES, default=1)

    class Meta:
        verbose_name = 'Id движка yourls'
        verbose_name_plural = 'Id движка yourls'

    def __str__(self):
        return self.yourls_id
