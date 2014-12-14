from django.test import TestCase
from django.core.urlresolvers import reverse
from todolist.models import ToDo

import datetime

class TodoListView(TestCase):

    def test_shows_current_date_in_index(self):
        resp = self.client.get(reverse('todolist:index'))
        dateToday = datetime.date.today()    
        self.assertContains(resp, dateToday.strftime('%b %d, %Y'))
        self.assertTemplateUsed(resp, 'index.html')

    def test_show_one_todo_index(self):
        ToDo.objects.create(description='todo list 1', isDone=False,
                                   dateAdded=datetime.date.today())
        dateToday = datetime.date.today()    

        resp = self.client.get(reverse('todolist:index'))

        self.assertContains(resp, dateToday.strftime('%b %d, %Y'))
        self.assertContains(resp, 'todo list 1')
        self.assertContains(resp, 'False')
        self.assertTemplateUsed(resp, 'index.html')
        
    def test_show_two_todo_index(self):
        ToDo.objects.create(description='todo list 1', isDone=False,
                                   dateAdded=datetime.date.today())
        ToDo.objects.create(description='todo list 2', isDone=True,
                                   dateAdded=datetime.date.today())

        dateToday = datetime.date.today()    

        resp = self.client.get(reverse('todolist:index'))

        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, dateToday.strftime('%b %d, %Y'))

        self.assertContains(resp, 'todo list 1')
        self.assertContains(resp, 'False')
        self.assertTemplateUsed(resp, 'index.html')

        self.assertContains(resp, 'todo list 2')
        self.assertContains(resp, 'True')
