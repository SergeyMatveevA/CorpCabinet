import os

ST_NEW = 'new'
ST_PROC = 'processing'
ST_ERR = 'error'
ST_FIN = 'final'
PROCESSING_STATE = (
    (ST_NEW, 'Не обработано'),
    (ST_PROC, 'В процессе обработки'),
    (ST_ERR, 'Ошибка обработки'),
    (ST_FIN, 'Обработка завершена')
)

NEW_SERVER = 'NEW'
MEGAFON_SERVER = 'MF'
CAR_SERVER = 'CAR'
SERVERS_NAMES = (
    (NEW_SERVER, 'Новый сервер'),
    (MEGAFON_SERVER, 'Мегафоновский сервер'),
    (CAR_SERVER, 'Автомобильный сервер'),
)

# Адреса файловых серверов нипо
SERVERS_ADDRESS = {
    'NEW': os.path.join('/mnt/NEW_SERVER_SHARE'),
    'MF': os.path.join('/mnt/MEGAFON_SERVER_SHARE'),
    'CAR': os.path.join('/mnt/CAR_SERVER_SHARE')
}
# Адреса шар с аудио-записями нипы
AUDIO_SHARES = {
    'NEW': os.path.join('/mnt/NEW_SERVER_AUDIO')
}

# Путь хранения стратификаций катишных проектов
STRATS_PATH = './media/strats/'

# типы квот
MM_QUOTA = 'many-to-many'
SL_QUOTA = 'slavery'
MS_QUOTA = 'master'
CN_QUOTA = 'concurrent'
# Заглушки для полей с номерами телефона, email или vin которые используются дилерами на смарт-дате вместо пустышек
base_plug = (
    'отказ от передачи данных', 'отказ  от передачи данных', 'Отказ', '_', 'otkaz@mail.ru', 'Net@mail.ru', 'bk@bk.ru'
    'Введите номер с указанием телефонного кода населённого пункта. Формат - 11 знаков через ведущую 8. Поле, не обязательное для заполнения',
    '-', '.', 'ОТСУТСТВУЕТ', 'отсутствует', 'отказ', 'нет@mail.ru', 'нет E-mail', 'нет', 'Нет', 'н/д',
    'Введите e-mail. Поле обязательно при условии, что дано разрешение на коммуникацию с контактным лицом в канале "E-mail"',
    '-', '--', '@', '1@1.RU', '1@gmail.com', '1@mail.ru', '1@MAIL.RU', '1@net.ru', '1@q.ru', '111@MAIL.RU',
    '123@1223.ru', 'net@mail.ru'
)
