from django.test import TestCase
from todolist.models import ToDo

class TodoList(TestCase):

    def test_create_instance_of_to_do(self):
        todo = ToDo()
