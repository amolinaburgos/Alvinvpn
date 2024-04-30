from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('http/', views.http, name="http"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.projectDetail, name="projectsDetail"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks2/', views.listarTareas2, name="tasks2"),
    path('tasks2/<int:task2_id>', views.detalleTareas, name="detalleTareas"),
    path('tasks2/<int:task2_id>/tareaCompleta', views.tareaCompleta, name="tareaCompleta"),
    path('tasks2/<int:task2_id>/tareaEliminar', views.tareaEliminar, name="tareaEliminar"),
    path('tasks2/todas', views.listarTareas2all, name="listarTareas2all"),
    path('persona/', views.persona, name="persona"),
    path('requerimiento1/', views.requerimiento1, name="requerimiento1"),
    path('crearTarea/', views.crearTarea, name="crearTarea"),
    path('crearProyecto/', views.crearProyecto, name="crearProyecto"),
    path('crearPersona/', views.crearPersona, name="crearPersona"),
    path('signup/', views.signup, name="signup"),
    path('ingreso/', views.ingreso, name="ingreso"),
    path('egreso/', views.egreso, name="egreso"),
    path('singout/', views.singout, name="singout"),
    path('signin/', views.signin, name="signin"),
    path('crearTarea2/', views.crearTarea2, name="crearTarea2"),
    path('tareaVerdatos/', views.tareaVerdatos, name="tareaVerdatos"),
    path('tareaModificarpersona/<int:persona_id>', views.tareaModificarpersona, name="tareaModificarpersona"),
    path('tareaModificartask/<int:task_id>', views.tareaModificartask, name="tareaModificartask"),

    
    
    ]

#Tareas que quiero realizar:
# - Mostrar listados seleccionando filtro
# - Cargardatos, almacenarlos en la base, poder consutlarlos y modificarloss