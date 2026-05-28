from django import forms
from .models import Alumno, Curso, NotaAlumnoPorCurso


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['codigo', 'nombre', 'correo']


class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursofuelds = ['codigo', 'curso', 'nota']


class NotaAlumnoPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoPorCurso
        fields = ['alumno', 'curso', 'nota']