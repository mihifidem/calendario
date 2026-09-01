from datetime import datetime

from django.db.models import Q
from django.shortcuts import redirect, render

from agenda.models import Categoria, Evento

# Create your views here.
def home(request):
    return render(request, "agenda/home.html")


def eventos(request):
    busqueda = request.GET.get("q", "").strip()
    categoria_id = request.GET.get("categoria", "")
    campo_orden = request.GET.get("orden", "fecha_inicio")
    direccion = request.GET.get("direccion", "asc")

    eventos = Evento.objects.all()

    if busqueda:
        eventos = eventos.filter(
            Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda)
        )

    if categoria_id:
        eventos = eventos.filter(categoria__id=categoria_id)

    if campo_orden == "titulo":
        orden = "titulo"
    else:
        orden = "fecha_inicio"

    if direccion == "desc":
        orden = "-" + orden

    eventos = eventos.order_by(orden)

    categorias = Categoria.objects.all()
    cantidad_eventos = eventos.count()
    context = {
        "data": eventos,
        "cantidad_eventos": cantidad_eventos,
        "busqueda": busqueda,
        "categorias": categorias,
        "categoria_seleccionada": categoria_id,
        "orden": campo_orden,
        "direccion": direccion,
    }
    return render(request, "agenda/eventos.html", context)


def crear_evento(request):
    categorias = Categoria.objects.all()
    context = {
        "categorias": categorias,
    }
    return render(request, "agenda/crear.html", context)


def crear_tarea(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        categoria_id = request.POST.get("categoria")

        if titulo and fecha_inicio and fecha_fin and categoria_id:
            try:
                inicio = datetime.strptime(fecha_inicio, "%Y-%m-%dT%H:%M")
                fin = datetime.strptime(fecha_fin, "%Y-%m-%dT%H:%M")
            except ValueError:
                return redirect("crear_evento")

            categoria = Categoria.objects.get(id=categoria_id)
            evento = Evento.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha_inicio=inicio,
                fecha_fin=fin,
            )
            evento.categoria.add(categoria)
            return redirect("eventos")

    return redirect("crear_evento")