from django.shortcuts import render


def huindai_finish_control(request):
    """Инструкция по закртию квот Хёндай"""
    return render(request, 'fw/cati/huindai_contact_check.html')


def make_appointment(request):
    """Инструкция по установке договоренности в нипо интервьюером"""
    return render(request, 'fw/cati/set_appointment.html')


def make_appointment_range(request):
    """Инструкция по установке договоренности в нипо интервьюером"""
    return render(request, 'fw/cati/set_appointment_range.html')


def paste_to_excel(request):
    """Инструкция по вставке данных в Excel"""
    return render(request, 'fw/cati/paste_to_excel.html')
