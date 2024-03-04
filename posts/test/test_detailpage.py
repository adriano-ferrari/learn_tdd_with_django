from http import HTTPStatus

from django.test import TestCase
from model_bakery import baker

from ..models import Post


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = baker.make(Post)
        self.response = self.client.get(self.post.get_absolute_url())

    def test_detail_page_returns_correct_response(self):

        self.assertEqual(self.response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.response, "posts/detail.html")

    def test_detail_page_returns_correct_content(self):

        self.assertContains(self.response, self.post.title)
        self.assertContains(self.response, self.post.body)
