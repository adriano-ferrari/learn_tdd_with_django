from django.test import TestCase
from http import HTTPStatus
from model_bakery import baker
from ..models import Post


class HomepageTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/")
        self.post1 = baker.make(Post)
        self.post2 = baker.make(Post)

    def test_homepage_returns_correct_response(self):

        self.assertTemplateUsed(self.response, "posts/index.html")
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)
