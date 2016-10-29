from django import forms
from apps.cita.models import Cita
from apps.paciente.models import Paciente

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita

        fields = [
            'medico',
            'paciente',
            'sucursal',
            'fecha',
            'descripcion_sintomas',
            'tipo'
        ]
        labels = {
            'medico' : 'Médico',
            'paciente' : 'Nro. de Identificación',
            'sucursal' : 'Centro de Salúd',
            'fecha' : ' Fecha de Cita',
            'descripcion_sintomas' : 'Describa los sintomas y otras consideraciones que considere pertinentes',
            'tipo' : 'Tipo de Consulta'
        }
        widgets = {
            'medico' : forms.Select(attrs={'class':'form-control'}),
            'paciente': forms.TextInput(attrs={'class':'form-control'}),
            'sucursal': forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'descripcion_sintomas': forms.Textarea(attrs={'class':'form-control'}),
            'tipo': forms.RadioSelect(attrs={'class':'form-control'})
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'cedula',
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'telefono',
            'peso',
            'estatura'
        ]
        labels = {
            'cedula' : 'Cedula',
            'nombre' : 'Nombres',
            'apellido' : 'Apellidos',
            'fecha_nacimiento' : 'Fecha de Nacimiento',
            'telefono' : 'Telefono',
            'peso' : 'Peso',
            'estatura':'Estatura'
        }
        widgets = {
            'cedula':forms.TextInput(),
            'nombre':forms.TextInput(),
            'apellido':forms.TextInput(),
            'fecha_nacimiento' : forms.DateInput(),
            'telefono' : forms.TextInput(),
            'peso': forms.TextInput(),
            'estatura' : forms.TextInput()
        }