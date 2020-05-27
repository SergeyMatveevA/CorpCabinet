from django.conf.urls import url

from user_docs.general import views

urlpatterns = [
    url(r'^yourls_interface$', views.yourls_interface, name='yourls_interface'),
]
