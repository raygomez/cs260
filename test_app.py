from django.test import TestCase
from todolist.models import ToDo

from django.contrib.auth.models import User

class CS260App(TestCase):

    def setUp(self):
        
        User.objects.create_user("user", "user@user.com", "user")
        self.client.login(username="user", password="user")

    def test_if_app_is_accessible_root(self):
        resp = self.client.get('');
        self.assertEqual(200, resp.status_code)
    
    def test_if_app_is_accessible(self):
        resp = self.client.get('/todolist/');
        self.assertEqual(200, resp.status_code)
