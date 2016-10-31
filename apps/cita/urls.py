from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.cita.views import CitaCreate, CitaListar, buscarPaciente3

app_name = 'cita'

urlpatterns=[

    url(r'^nueva_cita$', login_required(CitaCreate.as_view()), name='cita_crear'),
    url(r'^listar', login_required(CitaListar.as_view()), name='mis_citas'),
    url(r'^user_id/(?P<pk>\d+)/$', login_required(buscarPaciente3.as_view()), name='buscar_paciente')
]