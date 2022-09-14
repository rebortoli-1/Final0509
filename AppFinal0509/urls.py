from django.urls import path
from AppFinal0509 import views
from django.contrib.auth.views import LogoutView
urlpatterns =[
    path('', views.inicio, name="inicio"),
    path ('inicio', views.inicio,name="inicio"),
    path ('proyectosFormulario', views.proyectosFormulario,name="proyectosFormulario"),
    path ('metricasFormulario', views.metricasFormulario,name="metricasFormulario"),
    #CRUD
    path ('leerProyectos', views.leerProyectos,name="leerProyectos"),
    path ('eliminarProyectos/<proyecto_nombre>', views.eliminarProyecto,name="eliminarProyectos"),
    path ('editarProyectos/<proyecto_nombre>', views.editarProyecto,name="editarProyectos"),
    path('metrica/list', views.MetricaList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.MetricaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.MetricaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.MetricaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.MetricaDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='Login'),   
    path('register', views.register, name='register'),   
    path('logout', LogoutView.as_view(template_name='AppFinal0509/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('about', views.about, name="about"),

]