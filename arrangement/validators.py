import os

from django.core.exceptions import ValidationError


def validate_file_type(value, extenions):
    """Проверить коорректность типа файла
    :param extenions: Допустимые типы файлов
    :type extenions: list
    :param value: Проверяемый файл
    """
    ext = os.path.splitext(value.name)[1]
    if ext not in extenions:
        raise ValidationError('Загруженный тип файла ({load_ext}) не входит в список допустимых ({exts})'.format(
            load_ext=ext,
            exts=', '.join(extenions)
        ))


def xlsx_validate(value):
    """Валидатор xlsx-файлов"""
    return validate_file_type(value, ['.xlsx'])
