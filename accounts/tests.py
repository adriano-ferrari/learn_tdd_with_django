from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegistrationForm

# Create your tests here.


class AccountsCreationTests(TestCase):
    def setUp(self):
        self.form_class = UserRegistrationForm

    def test_signup_page_exists(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, 'Create your account today')

    def test_signup_form_works_correctly(self):
        form = self.form_class()

        self.assertTrue(issubclass(UserRegistrationForm, UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data = {
            'email': 'testuser@app.com',
            'username': 'testuser',
            'password1': 'p4ssword123###',
            'password2': 'p4ssword123###',
        }
        form = self.form_class(sample_data)
        self.assertTrue(form.is_valid())
