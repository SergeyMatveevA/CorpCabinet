from datetime import datetime as dt
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from cabinet.forms import SurveyStatForm
from cabinet.lib import cabinet_empty_render, get_view_content, get_stratification_content, get_fw_monirot_content
from sv.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def dialing_sample(request):
    """
    Отрисовать каунты по респонс-кодам сэмпла
    """
    page_name = 'Статусы интервью (Статистика использования базы)'
    form = SurveyStatForm()
    if request.method == "POST":
        return get_view_content(request, page_name, 1)
    else:
        return cabinet_empty_render(
            request, form, page_name, 'start_page', 'cabinet/dialing.html', dt.now().date(), dt.now().date()
        )


@login_required(login_url=LOGIN_URL)
def dialing_contact_log(request):
    """
    Отрисовать каунты по респонс-кодам контакт-лога
    """
    page_name = 'Статусы звонков (Статистика дозвона)'
    form = SurveyStatForm()
    if request.method == "POST":
        return get_view_content(request, page_name, 2)
    else:
        return cabinet_empty_render(
            request, form, page_name, 'start_page', 'cabinet/dialing.html', dt.now().date(), dt.now().date()
        )


def help(request):
    """Справка"""
    return render(request, 'cabinet/help.html')


@login_required(login_url=LOGIN_URL)
def stratification(request):
    """
    Отобразить стратификацию проекта
    """
    page_name = 'Стратификация проекта'
    form = SurveyStatForm()
    if request.method == "POST":
        return get_stratification_content(request, page_name)
    else:
        return cabinet_empty_render(request, form, page_name, 'start_page', 'cabinet/stratification.html')


def fieldwork_control(request):
    """
    Утилита мониторинга работы интервьюеров
    """
    page_name = 'Работа интервьюеров'
    form = SurveyStatForm()
    if request.method == "POST":
        return get_fw_monirot_content(request, page_name)
    else:
        return cabinet_empty_render(request, form, page_name, 'start_page', 'cabinet/interviewers_performance.html')
