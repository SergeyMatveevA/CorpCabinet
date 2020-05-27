from django.db import models


class Yourls2Log(models.Model):
    click_id = models.AutoField(primary_key=True)
    click_time = models.DateTimeField()
    shorturl = models.CharField(max_length=200)
    referrer = models.CharField(max_length=200)
    user_agent = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=41)
    country_code = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'yourls_2_log'
        verbose_name = 'Лог использования короткой ссылки'
        verbose_name_plural = 'Логи использования коротких ссылок'


class Yourls2Options(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(max_length=64)
    option_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'yourls_2_options'
        unique_together = (('option_id', 'option_name'),)


class Yourls2Url(models.Model):
    keyword = models.CharField('Id в yourls', primary_key=True, max_length=200)
    url = models.TextField('Проектная ссылка')
    title = models.TextField('Текст для предзагрузки', blank=True, null=True)
    timestamp = models.DateTimeField('Дата создания')
    ip = models.CharField('Ip узла с которого создали ссылку', max_length=41)
    clicks = models.PositiveIntegerField('Количество кликов', default=0)

    def short_link(self):
        return 'opros.ipsos.ru/{}'.format(self.keyword)

    def __str__(self):
        return 'opros.ipsos.ru/{}'.format(self.keyword)


    class Meta:
        managed = False
        db_table = 'yourls_2_url'
        verbose_name = 'Короткая ссылка'
        verbose_name_plural = 'Короткие ссылки'


class YourlsLog(models.Model):
    click_id = models.AutoField(primary_key=True)
    click_time = models.DateTimeField()
    shorturl = models.CharField(max_length=200)
    referrer = models.CharField(max_length=200)
    user_agent = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=41)
    country_code = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'yourls_log'
        verbose_name = 'Лог использования короткой ссылки'
        verbose_name_plural = 'Логи использования коротких ссылок проектов'


class YourlsOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(max_length=64)
    option_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'yourls_options'
        unique_together = (('option_id', 'option_name'),)


class YourlsUrl(models.Model):
    keyword = models.CharField('Id в yourls', primary_key=True, max_length=200)
    url = models.TextField('Проектная ссылка')
    title = models.TextField('Текст для предзагрузки', blank=True, null=True)
    timestamp = models.DateTimeField('Дата создания')
    ip = models.CharField('Ip узла с которого создали ссылку', max_length=41)
    clicks = models.PositiveIntegerField('Количество кликов', default=0)

    def short_link(self):
        return 'mbr.ipsos.ru/{}'.format(self.keyword)

    def __str__(self):
        return 'mbr.ipsos.ru/{}'.format(self.keyword)

    class Meta:
        managed = False
        db_table = 'yourls_url'
        verbose_name = 'Короткая ссылка'
        verbose_name_plural = 'Короткие ссылки проектов'
