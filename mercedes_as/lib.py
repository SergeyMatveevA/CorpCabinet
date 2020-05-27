import numpy as np
import pandas as pd

from arrangement.lib import check_duplicate, check_file_headers
from mercedes_as.models import WaveBase, ST_ERR


def first_stage_base_processing(base):
    """
    Первый этап обработки базы, функционал Насти Р.
    :type base: WaveBase
    :return:
    """
    if check_file_headers(r'./mercedes_as/docs/mercedes_as_base_template.xlsx', base.smartdata_base.path):
        contacts = pd.read_excel(base.smartdata_base.path, dtype=str)
    else:
        base.state = ST_ERR
        base.comments = 'Загруженная база не соответствует шаблону'
        base.save()
        return

    # Перекодировать коды ДЦ
    recode_dealers = {'anonymous': 'anonymous'}
    separate_dealers = {'anonymous': {'anonymousX': 100}}

    for row in contacts.iterrows():
        if row[1]['Код дилера'] in recode_dealers:
            contacts.loc[row[0], 'Код дилера'] = recode_dealers[row[1]['Код дилера']]
        elif row[1]['Код дилера'] in separate_dealers:
            contacts.loc[row[0], 'Код дилера'] = separate_dealers[row[1]['Код дилера']][row[1]['Комментарий']]

    # Проверить на дубли по номеру телефона, VIN и email
    check_duplicate(contacts, [('Стационарный телефон', 'Мобильный телефон'), ('E-mail', ), ('VIN номер ам', )])

    # Проверить валидность контактов
    neg_answers = [np.NaN, '2', '-']
    contacts.loc[
        (contacts['ResponseCode'] == '') & (contacts['Согласие на использование ПД'].isin(neg_answers)),
        'ResponseCode'] = 'Отказ'
    contacts.loc[
        (contacts['ResponseCode'] == '') & (contacts['Тип прохода'] == '1'), 'ResponseCode'
    ] = 'Внутренний заказ-наряд'
    contacts.loc[
        (contacts['Дата обслуживания'].str[3:5] != contacts['Код волны'].str[0:2]) &
        (contacts['ResponseCode'] == ''), 'ResponseCode'] = 'Дата обслуживания не подходит для исследования'
    contacts.loc[
        (contacts['Дата первой регистрации ам'].isin(
            [np.NaN, '', '-', '00.00.00', '00.00.0000', '01.01.0101', '01.01.1900',
             r'"Введите дату первой регистрации  а/м  ""Мерседес-Бенц""DD.MM.YYYY"', 'н/д', 'нет']
        )) & (contacts['ResponseCode'] == '') & (contacts['Тип прохода'] == '2'), 'ResponseCode'] = 'Нет ДПР'
    contacts.loc[
        (contacts['ResponseCode'] == '') & (contacts['Фамилия контактного лица '] is np.NaN) &
        (contacts['Имя контактного лица '] is np.NaN) & (contacts['Отчество контактного лица '] is np.NaN),
        'ResponseCode'] = 'Нет ФИО контактного лица'
    contacts.loc[
        (contacts['ResponseCode'] == '') & (contacts['Фамилия мастера-приёмщика'] is np.NaN) &
        (contacts['Имя мастера- приёмщика'] is np.NaN) & (contacts['Отчество мастера- приёмщика'] is np.NaN),
        'ResponseCode'] = 'Нет ФИО мастера'
    contacts.loc[
        (contacts['ResponseCode'] == '') & (contacts['Дата обслуживания'].str[3:5] != contacts['Код волны'].str[0:2]),
        'ResponseCode'] = 'Дата обслуживания не подходит для исследования'
    contacts.loc[
        (contacts['ResponseCode'] == '') & ((contacts['Фамилия контактного лица '].str.contains('ООО')) |
        (contacts['Имя контактного лица '].str.contains('ООО')) |
        (contacts['Отчество контактного лица '].str.contains('ООО'))), 'ResponseCode'] = 'Юр. Лицо'
    contacts.loc[
        (contacts['ResponseCode'] == '') & (contacts['Разрешение на контакт по телефону'].isin(neg_answers)) &
        (contacts['Разрешение на контакт по e-mail'].isin(neg_answers)) &
        (contacts['Разрешение на контакт по sms'].isin(neg_answers)), 'ResponseCode'] = 'Отказ от коммуникаций'
    contacts.loc[
        (contacts['ResponseCode'] == '') & (contacts['VIN номер ам'].str.len() != 17), 'ResponseCode'] =\
        'Некорректный VIN'
