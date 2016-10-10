from django.conf.urls import url
from apps.cita.views import index

urlpatterns=[
    url(r'^$', index)
]