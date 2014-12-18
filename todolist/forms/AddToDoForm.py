from django.forms import ModelForm
from todolist.models import ToDo

class AddToDoForm(ModelForm):
    class Meta:
        model = ToDo
        