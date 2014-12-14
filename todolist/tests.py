from django.test import TestCase
from todolist.models import ToDo

class TodoList(TestCase):

    def test_create_instance_of_to_do(self):
        todo = ToDo.objects.create(description='todo list 1', isDone=False,
            dateAdded=datetime.date.today())
        self.assertEqual("todo list 1", todo.description)
        self.assertTrue(not(todo.isDone))
        self.assertEqual(datetime.datetoday(), todo.dateAdded)
