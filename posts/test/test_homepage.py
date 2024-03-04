from django.test import TestCase
from http import HTTPStatus
from model_bakery import baker
from ..models import Post


class HomepageTest(TestCase):
    def setUp(self):
        self.post1 = baker.make(Post)
        self.post2 = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, "sample post 1")
        self.assertContains(response, "sample post 2")
