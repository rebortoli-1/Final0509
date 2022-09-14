from django.shortcuts import render

#from Final0509.AppFinal0509.models import Proyecto
from AppFinal0509.models import Proyecto,Metrica
from AppFinal0509.forms import ProyectoFormulario,MetricaFormulario
#from Final0509 import AppFinal0509


# Create your views here.
def inicio(request):

      return render(request, "AppFinal0509/inicio.html")

#def metrica(request):

 #     return render(request, "AppFinal0509/metricas.html")

from  AppFinal0509.forms import ProyectoFormulario,MetricaFormulario

def proyectosFormulario(request):
      if request.method == "POST":
            
                  miFormulario = ProyectoFormulario(request.POST)
                  print(miFormulario)

                  if miFormulario.is_valid:
                        informacion=miFormulario.cleaned_data
                        proyecto=Proyecto(nombre=informacion["nombre"],jefatura=informacion["jefatura"],gerencia=informacion["gerencia"],devops=informacion["devops"])
                        proyecto.save()
                        return render (request,"AppFinal0509/inicio.html")
      else:
            miFormulario=ProyectoFormulario()
      
      return render (request, "AppFinal0509/proyectosFormulario.html",{"miFormulario":miFormulario})      


def metricasFormulario(request):
      if request.method == "POST":
            
                  miFormulario = MetricaFormulario(request.POST)
                  print(miFormulario)

                  if miFormulario.is_valid:
                        informacion=miFormulario.cleaned_data
                        metrica=Metrica(nombre=informacion["nombre"],proyecto=informacion["proyecto"],observacion=informacion["observacion"])
                        metrica.save()
                        return render (request,"AppFinal0509/inicio.html")
      else:
            miFormulario=MetricaFormulario()
      
      return render (request, "AppFinal0509/metricasFormulario.html",{"miFormulario":miFormulario})          

##CRUD##########################
def leerProyectos(request):
      proyectos=Proyecto.objects.all()#trae todos los proyectos
      contexto = {"proyectos":proyectos}
      return render (request, "AppFinal0509/leerProyectos.html",contexto)


def eliminarProyecto(request, proyecto_nombre):
      proyecto=Proyecto.objects.get(nombre=proyecto_nombre)
      proyecto.delete()

      #vuelve al menu
      proyectos=Proyecto.objects.all () #traigo todos los pry
      contexto= {"proyectos":proyectos}
      return render (request, "AppFinal0509/leerProyectos.html",contexto)

def editarProyecto(request, proyecto_nombre):

    # Recibe el nombre del proyecto que vamos a modificar
    proyecto = Proyecto.objects.get(nombre=proyecto_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = ProyectoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            proyecto.nombre = informacion['nombre']
            proyecto.jefatura = informacion['jefatura']
            proyecto.gerencia = informacion['gerencia']
            proyecto.devops = informacion['devops']

            proyecto.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppFinal0509/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProyectoFormulario(initial={'nombre': proyecto.nombre, 'jefatura': proyecto.jefatura,
                                                   'gerencia': proyecto.gerencia, 'devops': proyecto.devops})

    # Voy al html que me permite editar
    return render(request, "AppFinal0509/editarProyectos.html", {"miFormulario": miFormulario, "proyecto_nombre": proyecto_nombre})
################FIN DE CRUD######################

####CLASES BASADAS EN VISTAS###########################
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class MetricaList(ListView):

    model = Metrica
    template_name = "AppFinal0509/metrica_list.html"

class MetricaDetalle(DetailView):

    model = Metrica
    template_name = "AppFinal0509/metrica_detalle.html"

class MetricaCreacion(CreateView):

    model = Metrica
    success_url = "/AppFinal0509/metrica/list"
    fields = ['nombre', 'proyecto_ref', 'observacion']

class MetricaUpdate(UpdateView):

    model = Metrica
    success_url = "/AppFinal0509/metrica/list"
    fields = ['nombre','proyecto_ref', 'observacion']

class MetricaDelete(DeleteView):

    model = Metrica
    success_url = "/AppFinal0509/metrica/list"

################FIN DE CLASES BASADAS EN VISTAS

###LOGIN###############

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppFinal0509.forms import UserRegisterForm,UserEditForm

from django.contrib.auth.decorators import login_required

# Vista de login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppFinal0509/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppFinal0509/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppFinal0509/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppFinal0509/login.html", {"form": form})

##############REGISTAR USR

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppFinal0509/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
          # form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppFinal0509/registro.html" ,  {"form":form})


@login_required
def inicio(request):

    return render(request, "AppFinal0509/inicio.html")


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppFinal0509/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppFinal0509/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

def about(request):

      return render(request, "AppFinal0509/about.html")

