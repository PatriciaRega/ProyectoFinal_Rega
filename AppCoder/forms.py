from django import forms
from .models import Farmaco, Paciente, Medico, Solicitud, Avatar

class FormularioSolicitud(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['farmaco', 'cod_paciente', 'cod_medico', 'fecha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date', 'format': 'yyyy-mm-dd'})

class FormularioMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'email', 'cod_medico']

class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'cod_paciente']   

class FormularioFarmaco(forms.ModelForm):
    class Meta:
        model = Farmaco
        fields = ['nombre', 'matriz_biologica']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']