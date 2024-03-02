from django.test import TestCase
from django.contrib.auth import get_user_model
from model_bakery import baker
from ..models import Post

User = get_user_model()


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = baker.make(Post)
        self.assertEqual(str(post), post.title)
        self.assertTrue(isinstance(post, Post))


class PostAuthorTest(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.post = Post.objects.create(
            title="Test title", body="Test body", author=self.user
        )

    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))

    def test_post_belong_to_user(self):
        self.assertTrue(hasattr(self.post, "author"))
        self.assertEqual(self.post.author, self.user)