import os

from sv.settings import MEDIA_ROOT

UPLOAD_DIR = os.path.join(MEDIA_ROOT, './media/yourls/')

ANONYMOUS_ENGINE = 'ANONYMOUS.ru'
GENERAL_ENGINE = 'opros.ipsos.ru'
ENGINES = (
    (ANONYMOUS_ENGINE, 'Проекты anonymous (anonymous.ru)'),
    (GENERAL_ENGINE, 'Общий движок (anonymous.ru)'),
)

ID_MAP = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'j', 10: 'k', 11: 'm', 12: 'n', 13: 'p', 14: 'q',
    15: 'r', 16: 's', 17: 't', 18: 'u', 19: 'w', 20: 'x', 21: 'y', 22: 'z', 23: '0', 24: '1', 25: '2', 26: '3', 27: '4',
    28: '5', 29: '6', 30: '7', 31: '8', 32: '9'
}

ID_ALREADY_USED = 'Указанные в файле id уже используются. Необходимо сгенерировать другие или не использовать опцию ' \
                  '"id из файла"'
ID_NOT_FIT_YOURLS = 'Id в файле не подходят для движка коротких ссылок (должны состоять только из латинских символов ' \
                    'или цифр)'
YOURLS_DB_ERROR = 'Не удалось записать в БД yourls'
