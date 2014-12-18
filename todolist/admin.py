from django.contrib import admin
from todolist.models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    fields = ['description', 'dateAdded', 'isDone', 'user']
    list_display = ('description', 'dateAdded', 'isDone', 'user')
    
admin.site.register(ToDo, ToDoAdmin)