from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task, Persona, Ingreso, Egreso, Task2
from .forms import CrearNuevaTarea, CrearProyecto, CrearPersona, CrearTarea2
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def http(request):
    return HttpResponse('Hola mundo')

@login_required
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

@login_required
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

@login_required
def persona(request):
    persona = Persona.objects.all()
    return render(request, 'persona.html', {
        'persona': persona
    })

@login_required
def requerimiento1(request):
    projects = Project.objects.all()
    return render(request, 'requerimiento1.html', {
        'projects': projects}
    )

@login_required
def crearTarea(request):
    if request.method == 'GET':
        return render(request, 'crearTarea.html', {
            'form': CrearNuevaTarea()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=1)
    return redirect('tasks')

@login_required
def crearProyecto(request):
    if request.method == 'GET':
        return render(request, 'crearProyecto.html', {
            'form': CrearProyecto()
        })
    else:
        Project.objects.create(name=request.POST['name'])
    return redirect('projects')
@login_required

def crearPersona(request):
    if request.method == 'GET':
        return render(request, 'crearPersona.html', {
            'form': CrearPersona()
        })
    else:
        Persona.objects.create(name=request.POST['name'],
                               age=request.POST['age'],
                               dni=request.POST['dni'],
                               project_id=2)
        return redirect('persona')

@login_required
def projectDetail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'projectsDetail.html', {
        'project': project,
        'tasks': tasks
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect ('tasks2')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Nombre de usuario, ya existente'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'No coinciden los passwords'
        })


def singout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o password, incorrecto'
            })
        else:
            login(request, user)
            return redirect('tasks2')

@login_required
def crearTarea2(request):
    if request.method == 'GET':
        return render(request, 'crearTarea2.html', {
            'form': CrearTarea2
        })
    else:
        try:
            form = CrearTarea2(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect('tasks2')
        except ValueError:
            return render(request, 'crearTarea2.html', {
                'form': CrearTarea2,
                'error': 'Datos incorrectos'
            })
        
@login_required
def listarTareas2(request):
    tareas = Task2.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'task2.html', {
        'tareas': tareas
    })

def listarTareas2all(request):
    tareas = Task2.objects.all()
    return render(request, 'task2all.html', {
        'tareas': tareas
    })


@login_required
def listarTareas2allBASICO(request):
    tareas = Task2.objects.filter(user=request.user)
    return render(request, 'task2.html', {
        'tareas': tareas
    })

@login_required
def detalleTareas(request, task2_id):
    if request.method == 'GET':
        task = get_object_or_404(Task2, pk=task2_id) 
        form = CrearTarea2(instance=task)
        return render (request, 'task2Detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task2, pk=task2_id, user=request.user)
            form = CrearTarea2(request.POST, instance=task)
            form.save()
            return redirect('tasks2')
        except ValueError:
            return render (request, 'task2Detail.html', {'task': task, 'form': form, 'error': "Error actualizando"})


@login_required       
def tareaCompleta(request, task2_id):
    task = get_object_or_404(Task2, pk=task2_id, user=request.user)
    if request.method == "POST" :
        task.datecompleted = timezone.now()
        task.save()
        return redirect ('tasks2')
@login_required   
def tareaEliminar(request, task2_id):
    task = get_object_or_404(Task2, pk=task2_id, user=request.user)
    if request.method == "POST" :
        task.delete()
        return redirect ('tasks2')
    
@login_required
def detalleTareasBASICO(request, task2_id):
    task = Task2.objects.get(pk=task2_id)
    return render (request, 'task2Detail.html', { 'task': task })

@login_required
def tareaVerdatos(request):
    tasks = Task.objects.all()
    people = Persona.objects.all()
    return render(request, 'tareaVerdatos.html', {
        'tasks': tasks,
        'people': people
    })




@login_required
def ingreso(request):
    return render(request, 'ingreso.html')

@login_required
def egreso(request):
    return HttpResponse("hola egreso")



# from django.shortcuts import render

# Create your views here.
