from django.test import TestCase
from todolist.models import ToDo

class CS260App(TestCase):

    def test_if_app_is_accessible_root(self):
        resp = self.client.get('');
        self.assertEqual(200, resp.status_code)
    
    def test_if_app_is_accessible(self):
        resp = self.client.get('/todolist/');
        self.assertEqual(200, resp.status_code)
