from django.conf.urls import url

from apps.historiaclinica.views import index
urlpatterns = [
    url(r'^$', index)
]