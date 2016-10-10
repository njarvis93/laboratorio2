from django.conf.urls import url, include

from apps.paciente.views import index

urlpatterns = [
    url(r'^$', index)
]