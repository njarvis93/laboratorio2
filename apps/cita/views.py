from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from apps.paciente.models import Paciente
from apps.cita.forms import PacienteForm, CitaForm
from apps.cita.models import Cita
from django.utils import timezone

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

class BuscarPaciente(DetailView):
    model = Paciente
    def get_context_data(self, **kwargs):
        context = super(BuscarPaciente, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context