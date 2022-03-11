
from django.urls import path
from .views import inicio, otra_vista, numero_random, numero_usuario, cumpleaños, mi_plantilla

urlpatterns = [
    path('', inicio),
    path('otra_vista', otra_vista),
    path('numero-random/', numero_random),
    path('dame-random/<int:numero>', numero_usuario),
    path('edad/<int:año>', cumpleaños),
    path('mi_plantilla/', mi_plantilla),
]