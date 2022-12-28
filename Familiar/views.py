from django.shortcuts import render
from django.http import HttpResponse
from Familiar.models import Familiar


def crear_familiar(request):
    Familiar.objects.create(Nombre = 'José', Apellido = 'Díaz', Edad = 70, Esta_vivo = True)
    return HttpResponse('Se agrego nuevo familiar')

def lista_familiares(request):
    todos_los_familiares = Familiar.objects.all()
    context = {
        'Familia': todos_los_familiares,
    }
    return render(request, 'Lista_Familiares.html', context = context)