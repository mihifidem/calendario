from django.shortcuts import render

from agenda.models import Evento

# Create your views here.
def home(request):
    return render(request, "agenda/home.html")

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, "agenda/eventos.html", {"data": eventos})