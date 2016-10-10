from django.conf.urls import url
from apps.tratamiento.views import index

urlpatterns = [
    url(r'^$', index)
]