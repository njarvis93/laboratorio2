from django.conf.urls import url
from apps.medico.views import index_medico
urlpatterns = [
    url(r'^$', index_medico)
]