from django.conf.urls import url

from apps.enfermedad.views import index

urlpatterns=[
    url(r'^$', index)
]