from django.test import TestCase
from django.core.urlresolvers import reverse
import datetime

class TodoListView(TestCase):

    def test_shows_current_date_in_index(self):
        resp = self.client.get(reverse('todolist:index'))
        dateToday = datetime.date.today()    
        self.assertContains(resp, dateToday.strftime('%b %d, %Y'))
        self.assertTemplateUsed(resp, 'index.html')
