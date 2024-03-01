from django.test import TestCase
from http import HTTPStatus
from django.contrib.auth import get_user_model
from model_bakery import baker
from .models import Post

# Create your tests here.

User=get_user_model()


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = baker.make(Post)

        self.assertEqual(str(post), post.title)
        self.assertTrue(isinstance(post, Post))


class HomepageTest(TestCase):
    def setUp(self):
        self.post1 = baker.make(Post)
        self.post2 = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get('/')
        self.assertContains(response, 'sample post 1')
        self.assertContains(response, 'sample post 2')


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = baker.make(Post)

    def test_detail_page_returns_correct_response(self):
        response=self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html')

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertContains(response, self.post.created_at)


class PostAuthorTest(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.post = Post.objects.create(
            title='Test title',
            body='Test body',
            author=self.user
        )

    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))

    def test_post_belong_to_user(self):
        self.assertTrue(hasattr(self.post, 'author'))
        self.assertEqual(self.post.author, self.user)