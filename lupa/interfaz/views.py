from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Card
from .forms import CartaCreacionForm

# Create your views here.

def login(request):
    return render(request, 'login.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def pagina_prueba(request):
    return render(request, 'pagina_prueba.html')

def prueba(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'prueba.html', context)

def crear_carta(request):
    if request.method == 'POST':
        form = CartaCreacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carta creada correctamente.')
            return redirect('prueba')
        else:
            messages.error(request, 'No se ha podido crear la carta. Revisa los errores en el formulario.')
    else:
        form = CartaCreacionForm()
    return render(request, 'cartas/crear_carta.html', {'form': form})

def modificar_carta(request, id):
    carta = get_object_or_404(Card, id=id)
    if request.method == 'POST':
        form = CartaCreacionForm(request.POST, request.FILES, instance=carta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carta modificado correctamente.')
            return redirect('prueba')
        else:
            messages.error(request, "No se ha podido modificar la carta.")
    else:
        form = CartaCreacionForm(instance=carta)
    context = {
        'form': form,
        'mensaje_correcto': messages.get_messages(request),
        'mensaje_incorrecto': messages.get_messages(request),
    }
    return render(request, 'cartas/modificar_carta.html', context)

def eliminar_carta(request, id):
    carta = get_object_or_404(Card, id=id)
    carta.delete()
    messages.success(request, 'Carta eliminada correctamente.')
    return redirect('prueba')

def register(request):
    return render(request, 'register.html')