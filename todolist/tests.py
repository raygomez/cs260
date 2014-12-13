from django.test import TestCase
from todolist.models import ToDo

class TodoList(TestCase):

    def test_create_instance_of_to_do(self):
        todo = ToDo()

    def test_if_app_is_accessible(self):
        resp = self.client.get('/todolist/');
        self.assertEqual(200, resp.status_code)
