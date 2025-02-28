# cursos/views.py
from django.shortcuts import render
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'cursos/detalle_curso.html', {'curso': curso})
