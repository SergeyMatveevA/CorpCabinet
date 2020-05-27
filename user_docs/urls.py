from django.urls import path, include

urlpatterns = [
    path('fw/', include('user_docs.fw.urls')),
    path('dp/', include('user_docs.dp.urls')),
    path('general/', include('user_docs.general.urls')),
]