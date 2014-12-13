from django.test import TestCase

class TodoList(TestCase):

    def test_create_instance_of_to_do(self):
        todo = Todo()
