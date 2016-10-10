from django.conf.urls import url, include

from apps.centrodesalud.views import index

urlpatterns = [
    url(r'^$', index)
]