from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("eventos/", views.eventos, name="eventos"),
    path("crear/", views.crear_evento, name="crear_evento"),
    path("crear_tarea/", views.crear_tarea, name="crear_tarea"),
]   

