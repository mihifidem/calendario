from django.utils import timezone
from datetime import timedelta

from agenda.models import Evento, Categoria


# Recuperar categorías que YA existen
trabajo = Categoria.objects.get(nombre="Trabajo")
estudio = Categoria.objects.get(nombre="Estudio")
salud = Categoria.objects.get(nombre="Salud")


# Crear evento
evento1 = Evento.objects.create(
    titulo="Reunión de equipo",
    descripcion="Revisar las tareas pendientes del proyecto.",
    fecha_inicio=timezone.now(),
    fecha_fin=timezone.now() + timedelta(hours=1)
)

# Relacionarlo con una categoría existente
evento1.categoria.add(trabajo)