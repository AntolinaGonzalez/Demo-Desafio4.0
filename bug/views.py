from django.shortcuts import render, redirect
from .models import UploadImages, UploadTarget
from .forms import AnalizarImagenes, CargarTarget
# Create your views here.
cont = 1
def paginaInicio(request):
    imagenes = AnalizarImagenes()
    target = CargarTarget()
    contexto = {
        'imagenes': imagenes,
        'target': target
    }
    if request.method == "POST":
        imagenes = AnalizarImagenes(request.POST or None, request.FILES or None)
        target = CargarTarget(request.POST or None, request.FILES or None)
        contexto ={
            'imagenes':imagenes,
            'target':target
        }
        if imagenes.is_valid():
            imagenes.save()
            return redirect('bug:result')
        if target.is_valid():
            target.save()
            return redirect('bug:index')
        
    return render(request, 'index.html',contexto)

def analisisImagen(request):
    imagenes= UploadImages.objects.last()
    contexto = {
        'imagenes': imagenes
    }
    return render(request, 'analisisdeImagen.html', contexto)