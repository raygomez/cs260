from django.forms import ModelForm
from todolist.models import ToDo
from django.utils.translation import ugettext_lazy as _

class AddToDoForm(ModelForm):
    class Meta:
        model = ToDo
        exclude = ['isDone', 'dateAdded', 'user']
        labels = {
            'description' : _(' '),
        }