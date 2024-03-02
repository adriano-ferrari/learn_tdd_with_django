from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

# Create your tests here.


class AccountsCreationTests(TestCase):
    def test_signup_page_exists(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, 'Create your account today')
