from django import forms


#class FormularioSolicitudes(forms.Form):    
    #farmaco = forms.CharField(max_length=60)
    #cod_paciente = forms.CharField(max_length=30)
    #cod_medico = forms.CharField(max_length=30)
    #fecha = forms.DateField()

class FormularioMedico(forms.Form):    
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    cod_medico = forms.CharField(max_length=10)
    