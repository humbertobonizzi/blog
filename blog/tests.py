from django.test import TestCase
from django.urls import resolve
#from blog.views import home_page

# Create your tests here.
home_page = None

class HomePageTest(TestCase):

    #Testa se o caminho root leva a alguma view
    def test_root_home(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
