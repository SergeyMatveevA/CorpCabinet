from django.shortcuts import render


def config_survey_call_times(request):
    """Инструкция по конфигурации проектов c парралельным использованием CallInterval и TimeDifference"""
    return render(request, 'dp/scr/config_survey_call_times.html')
