from django.urls import path, include

urlpatterns = [
    path('scr/', include('user_docs.dp.scr.urls'))
]