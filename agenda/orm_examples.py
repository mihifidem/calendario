from agenda.models import Categoria, Evento


def get_orm_examples():
    """Devuelve un conjunto de ejemplos de ORM sin modificar la base de datos."""
    eventos = list(Evento.objects.order_by("fecha_inicio")[:5].values_list("titulo", flat=True))
    categorias = list(Categoria.objects.values_list("nombre", flat=True)[:10])

    return {
        "commands": [
            {
                "title": "all()",
                "query": "Evento.objects.all()",
                "description": "Obtiene todos los registros de la tabla.",
                "result": eventos,
            },
            {
                "title": "filter()",
                "query": "Evento.objects.filter(titulo__icontains='reunion')",
                "description": "Filtra eventos por un criterio.",
                "result": list(
                    Evento.objects.filter(titulo__icontains="reunion").values_list("titulo", flat=True)[:5]
                ),
            },
            {
                "title": "get()",
                "query": "Evento.objects.get(id=1)",
                "description": "Devuelve un único resultado o lanza DoesNotExist.",
                "result": list(Evento.objects.filter(id=1).values_list("titulo", flat=True)[:1]),
            },
            {
                "title": "create()",
                "query": "Evento.objects.create(...)",
                "description": "Crea un nuevo registro en una sola línea.",
                "result": ["Ejemplo: Evento.objects.create(titulo='Nuevo evento', descripcion='...', fecha_inicio=..., fecha_fin=...)"],
            },
            {
                "title": "update()",
                "query": "Evento.objects.filter(...).update(...)",
                "description": "Actualiza varios registros sin guardar cada objeto individualmente.",
                "result": ["Ejemplo: Evento.objects.filter(id=1).update(descripcion='Actualizado')"],
            },
            {
                "title": "exclude()",
                "query": "Evento.objects.exclude(titulo__icontains='reunion')",
                "description": "Excluye resultados que coincidan con un filtro.",
                "result": list(
                    Evento.objects.exclude(titulo__icontains="reunion").values_list("titulo", flat=True)[:5]
                ),
            },
            {
                "title": "order_by()",
                "query": "Evento.objects.order_by('fecha_inicio')",
                "description": "Ordena la consulta por un campo.",
                "result": list(Evento.objects.order_by("fecha_inicio").values_list("titulo", flat=True)[:5]),
            },
            {
                "title": "values()",
                "query": "Evento.objects.values('id', 'titulo')",
                "description": "Devuelve diccionarios con campos seleccionados.",
                "result": list(Evento.objects.values("id", "titulo")[:3]),
            },
            {
                "title": "count()",
                "query": "Evento.objects.count()",
                "description": "Cuenta cuántos registros existen.",
                "result": [f"Total: {Evento.objects.count()}"],
            },
            {
                "title": "exists()",
                "query": "Evento.objects.filter(...).exists()",
                "description": "Comprueba si hay algún resultado.",
                "result": [f"Hay eventos: {Evento.objects.exists()}"],
            },
            {
                "title": "set()",
                "query": "evento.categoria.set([categoria1, categoria2])",
                "description": "Reemplaza todas las relaciones de ManyToMany.",
                "result": ["Ejemplo: evento.categoria.set([cat1, cat2])"],
            },
            {
                "title": "add()",
                "query": "evento.categoria.add(categoria3)",
                "description": "Añade nuevas relaciones de ManyToMany.",
                "result": ["Ejemplo: evento.categoria.add(categoria3)"],
            },
            {
                "title": "remove()",
                "query": "evento.categoria.remove(categoria3)",
                "description": "Elimina una relación concreta.",
                "result": ["Ejemplo: evento.categoria.remove(categoria3)"],
            },
            {
                "title": "clear()",
                "query": "evento.categoria.clear()",
                "description": "Elimina todas las relaciones de una colección ManyToMany.",
                "result": ["Ejemplo: evento.categoria.clear()"],
            },
            {
                "title": "Categorías",
                "query": "Categoria.objects.all()",
                "description": "Consulta de ejemplo para muchas relaciones.",
                "result": categorias,
            },
        ]
    }
