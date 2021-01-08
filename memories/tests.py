from django.test import TestCase, Client
from django.urls import reverse
from .models import Place
from django.contrib.auth.models import User


class MemoriesTest(TestCase):
    def setUp(self):

        user = User.objects.create(username='test_user', email='test@mail.com',
                                   first_name='FName', last_name='LName')
        user.set_password('pas123')
        user.save()
        self.user = user

    def test_anon(self):
        """
        Test that anon user is redirected to login page
        """
        client = Client()
        response = client.get(reverse('detail'))
        self.assertEqual(response.status_code, 302)

    def test_user_detail(self):
        """
        Test that authenticated user is allowed to get the page with all the information
        """
        client = Client()
        client.login(username='test_user', password='pas123')
        response = client.get(reverse('detail'))
        self.assertEqual(response.status_code, 200)

    def test_user_detail_context(self):
        """
        Test that detail-view returns a correct context
        """
        client = Client()
        client.login(username='test_user', password='pas123')
        response = client.get(reverse('detail'))
        self.assertEqual(len(self.user.place_set.all()), len(response.context['places']))

    def test_user_add_get(self):
        """
        Test that authenticated user is allowed to get the page for adding the memories
        """
        client = Client()
        client.login(username='test_user', password='pas123')
        response = client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)

    def test_user_add_post(self):
        """
        Test that authenticated user is redirected to detail page after sending data
        """
        client = Client()
        client.login(username='test_user', password='pas123')
        response = client.post(reverse('add'), {'name': 'testName', 'comment': 'testComment',
                                                'lat': '56', 'long': '92', 'author': self.user})
        self.assertEqual(response.status_code, 302)

    def test_user_add_post_twice(self):
        """
        Test that data from POST-request is stored in DB
        """
        size_before = Place.objects.count()
        client = Client()
        client.login(username='test_user', password='pas123')
        client.post(reverse('add'), {'name': 'testName1', 'comment': 'testComment1',
                                     'lat': '56', 'long': '92', 'author': self.user})
        client.post(reverse('add'), {'name': 'testName2', 'comment': 'testComment2',
                                     'lat': '92', 'long': '56', 'author': self.user})
        size_after = Place.objects.count()
        self.assertEqual(size_before + 2, size_after)
