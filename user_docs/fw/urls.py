from django.urls import path, include

urlpatterns = [
    path('cati/', include('user_docs.fw.cati.urls'))
]