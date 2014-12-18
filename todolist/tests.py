from django.test import TestCase
from todolist.models import ToDo
from django.contrib.auth.models import User
 
import datetime

class TodoList(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("user", "user@user.com", "user")

    def test_create_instance_of_to_do(self):
        todo = ToDo.objects.create(description='todo list 1', isDone=False,
            dateAdded=datetime.date.today(), user=self.user)
        self.assertEqual("todo list 1", todo.description)
        self.assertTrue(not(todo.isDone))
        self.assertEqual(datetime.date.today(), todo.dateAdded)
        self.assertEqual(self.user, todo.user)
