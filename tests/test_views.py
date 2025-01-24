import unittest
from django.test import Client, TestCase
from django.urls import reverse
from snippets.models import Snippet, Language
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.language = Language.objects.create(name='Python', slug='python')
        self.snippet = Snippet.objects.create(
            name='Test Snippet',
            description='Test Description',
            snippet='print("Hello, World!")',
            language=self.language,
            public=True,
            user=self.user
        )

    def test_public_snippet_list_view(self):
        response = self.client.get(reverse('public_snippets'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snippets/public_snippets.html')
        self.assertContains(response, 'Test Snippet')

    def test_snippet_detail_view(self):
        response = self.client.get(reverse('snippet_detail', kwargs={'id': self.snippet.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snippets/snippet_detail.html')
        self.assertContains(response, 'Test Snippet')

    def test_user_snippets_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user_snippets', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snippets/user_snippets.html')
        self.assertContains(response, 'Test Snippet')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snippets/login.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirección después del logout

    def test_index_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Snippet')

if __name__ == '__main__':
    unittest.main()
