from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from apps.paciente.models import Paciente
from apps.cita.forms import PacienteForm, CitaForm
from apps.cita.models import Cita
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.template import loader
# Create your views here.

class CitaCreate(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'medical/cita.html'
    success_url = reverse_lazy('cita:mis_citas')

class CitaListar(ListView):
    model = Cita
    template_name = 'medical/citas.html'
    paginate_by = 2

#def buscarPaciente(request, id_paciente):
#    paciente = get_object_or_404(Paciente, pk=id_paciente)
#    return HttpResponseRedirect(reverse('cita:cita_crear', args=(paciente,)))

class buscarPaciente3(DetailView):
    model = Paciente
    template_name = 'medical/cita.html'

