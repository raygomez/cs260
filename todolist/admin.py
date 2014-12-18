from django.contrib import admin
from todolist.models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    fields = ['description', 'dateAdded', 'isDone']
    list_display = ('description', 'dateAdded', 'isDone')
    
admin.site.register(ToDo, ToDoAdmin)