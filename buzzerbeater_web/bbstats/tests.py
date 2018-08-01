from django.test import TestCase

from . import views

from .models import Players

# Create your tests here.

class ViewTester(TestCase):

    def setUp(self):
        Players.objects.create(id=123, name='Kok')

    def test_get_totals(self):
        self.assertIsNone(views.get_totals('blalba'))

