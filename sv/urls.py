from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from sv import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('instructions/', include('user_docs.urls')),
    path('cabinet/', include('cabinet.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
