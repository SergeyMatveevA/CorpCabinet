from django.shortcuts import render


def yourls_interface(request):
    """Инструкция по созданию коротких ссылок в Yourls"""
    return render(request, 'general/yourls_interface.html')
