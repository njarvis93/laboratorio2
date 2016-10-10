from django.conf.urls import url
from apps.medico.views import index
urlpatterns = [
    url(r'^$', index)
]