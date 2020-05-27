from django import forms
from .models import Alumno , Asistencia


class AlumnoForm(forms.ModelForm):
    class Meta:
        model=Alumno
        fields=(
            'nombre',
            'legajo',
        )

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model=Asistencia
        fields=(
            'alumno',
            'fecha',
        )
    
