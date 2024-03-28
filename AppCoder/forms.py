from django import forms
from .models import Farmaco, Paciente, Medico

class FormularioSolicitud(forms.Form):    
    farmaco = forms.ModelChoiceField(queryset=Farmaco.objects.all(), empty_label=None)
    cod_paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), empty_label=None)
    cod_medico = forms.ModelChoiceField(queryset=Medico.objects.all(), empty_label=None)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class FormularioMedico(forms.Form):    
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    cod_medico = forms.CharField(max_length=10)

class FormularioPaciente(forms.Form):    
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    cod_paciente = forms.CharField(max_length=10)    

class FormularioFarmaco(forms.ModelForm):
    class Meta:
        model = Farmaco
        fields = ['nombre', 'matriz_biologica']

