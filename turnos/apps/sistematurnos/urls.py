from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^nuevo/', TurnoCreate.as_view(), name='Turno_crear'),
    url(r'^listar', TurnoList.as_view(), name='Turno_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', TurnoDelete.as_view(), name='Turno_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', TurnoUpdate.as_view(), name='Turno_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', TurnoShow.as_view(), name='Turno_mostrar'),
]