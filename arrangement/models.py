import os

from django.contrib.auth.models import User
from django.db import models

from arrangement.consts import SERVERS_NAMES, SERVERS_ADDRESS, STRATS_PATH
from arrangement.lib import stratification_reload

ST_AC = 'active'
ST_NA = 'not_active'
TASK_STATE = (
    (ST_AC, 'активная задача'),
    (ST_NA, 'неактивная зада'),
)


class Survey(models.Model):
    name = models.CharField('Имя проекта', max_length=150, null=True, blank=True)
    cati_programm_name = models.CharField('Имя программы проекта', max_length=7)
    server_name = models.CharField(max_length=16, choices=SERVERS_NAMES, blank=True, null=True)
    stratification = models.FileField('Стратификация проекта', blank=True, null=True, upload_to=STRATS_PATH)
    stratification_update_date = models.DateTimeField('Дата обновления стратифкации', blank=True, null=True)
    last_sample_activity = models.DateTimeField('Последняя активность в сэмпле', blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.cati_programm_name

    def stratification_update(self):
        strat_address = os.path.join(
            SERVERS_ADDRESS[self.server_name], self.cati_programm_name.title(),
            '{survey}s'.format(survey=self.cati_programm_name.title())
        )
        if os.path.exists(strat_address):
            if self.stratification_update_date != os.stat(strat_address).st_mtime:
                stratification_reload(self, strat_address)
        else:
            strat_address = strat_address.replace('SHARE', 'SHARE_old')
            if os.path.exists(strat_address):
                if self.stratification_update_date != os.stat(strat_address).st_mtime:
                    stratification_reload(self, strat_address)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class StandardTasks(models.Model):
    name = models.CharField('Задача', max_length=50)
    readable_name = models.CharField('Название задачи', max_length=50)
    state = models.CharField('Состояние задачи', max_length=10, choices=TASK_STATE, default=ST_AC)

    def __str__(self):
        return self.readable_name

    class Meta:
        verbose_name = 'Стандартная задача'
        verbose_name_plural = 'Стандартные задачи'


class ActiveJobs(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Проект')
    task = models.ForeignKey(StandardTasks, on_delete=models.CASCADE, verbose_name='Задача', related_name='sv_tasks')
    state = models.CharField('Состояние задачи', max_length=10, choices=TASK_STATE, default=ST_AC)
    expiration_date = models.DateField('Дата закрытия задачи', blank=True, null=True)

    def __str__(self):
        return '{task} {survey}'.format(task=self.task.readable_name, survey=self.survey.name)

    class Meta:
        verbose_name = 'Активное задание'
        verbose_name_plural = 'Активные задания'


class SurveyStratification(models.Model):
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
    numbers_of_appointments = models.IntegerField('Количество свежих договоренностей', default=0)
    numbers_of_no_answered = models.IntegerField('Количество не ответивших', default=0)
    numbers_of_eliminated = models.IntegerField('Количество использованных', default=0)
    percentage_of_target = models.CharField('Процент выполнения квоты', max_length=10, default=0)

    def __str__(self):
        if self.description:
            return self.description
        else:
            '%s %s'.format(self.field, self.field_val)


class Feedback(models.Model):
    content = models.TextField('Отзыв')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Обратная связь'
