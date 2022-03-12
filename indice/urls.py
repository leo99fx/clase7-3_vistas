
from django.urls import path
from .views import inicio, otra_vista, numero_random, numero_usuario, cumpleaños, mi_plantilla

urlpatterns = [
    path('', inicio, name="inicio"),
    path('otra_vista', otra_vista, name="otra_vista"),
    path('numero-random/', numero_random, name="numero-random"),
    path('dame-random/<int:numero>', numero_usuario, name="dame-random"),
    path('edad/<int:año>', cumpleaños, name="cumpleaños"),
    path('mi_plantilla/', mi_plantilla, name="mi_plantilla"),
]