from django.shortcuts import render, redirect
from .models import Alumno, Curso, NotaAlumnoPorCurso
from .forms import AlumnoForm, CursoForm, NotaAlumnoPorCursoForm


# ALUMNOS

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
        
    else:
        form = AlumnoForm()

    return render(request, 'academico/crear_alumno.html', {'form': form})


def lista_alumnos(request):
    alumnos = Alumno.objects.all()

    return render(request, 'academico/lista_alumnos.html', {
        'alumnos': alumnos
    })


# CURSOS

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
        
    else:
        form = CursoForm()

    return render(request, 'academico/crear_curso.html', {'form': form})


def lista_cursos(request):
    cursos = Curso.objects.all()

    return render(request, 'academico/lista_cursos.html', {
        'cursos': cursos
    })


# NOTAS

def crear_nota(request):
    if request.method == 'POST':
        form = NotaAlumnoPorCursoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_notas')
        
    else:
        form = NotaAlumnoPorCursoForm()
    
    return render(request, 'academico/crear_nota.html', {'form': form})


def lista_notas(request):
    notas = NotaAlumnoPorCurso.objects.all()

    return render(request, 'academico/lista_notas.html', {
        'notas': notas
    })