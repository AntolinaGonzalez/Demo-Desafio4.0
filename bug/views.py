from django.shortcuts import render, redirect
from .models import UploadImage
from .forms import AnalizarImagenes
# Create your views here.
cont = 1
def paginaInicio(request):
    imagenes = AnalizarImagenes()
    contexto = {
        'imagenes': imagenes
    }
    if request.method == "POST":
        imagenes = AnalizarImagenes(request.POST or None, request.FILES or None)
        contexto ={
            'imagenes':imagenes
        }
        if imagenes.is_valid():
            imagenes.save()
            return redirect('bug:result')
        
    return render(request, 'index.html',contexto)

def analisisImagen(request):
    imagenes= UploadImage.objects.last()
    contexto = {
        'imagenes': imagenes
    }
    return render(request, 'analisisdeImagen.html', contexto)