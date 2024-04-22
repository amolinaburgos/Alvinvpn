from django.contrib import admin
from .models import Project, Task, Persona, Task2

class Taskadmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Persona)
admin.site.register(Task2, Taskadmin)