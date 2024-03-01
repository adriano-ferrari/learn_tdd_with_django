from django.test import TestCase
from http import HTTPStatus
from .models import Post

# Create your tests here.


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = Post.objects.create(title="Test Post", body="Test Body")
        self.assertEqual(str(post), post.title)


class HomepageTest(TestCase):
    def setUp(self):
        post1 = Post.objects.create(
            title="sample post 1",
            body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin tristique semper. Nulla porttitor lorem leo, ut ornare leo lobortis ut. Phasellus ut finibus purus. In elementum a nibh nec cursus. Donec et nisl non mi mattis auctor. Praesent sit amet gravida nisl, vitae pulvinar diam. Duis vel pulvinar dui. Aenean a purus metus. Morbi et volutpat nulla, at congue ligula. Fusce tristique turpis vitae tincidunt ullamcorper. Sed vestibulum eros quis justo faucibus malesuada. Phasellus a eros venenatis, eleifend ex in, efficitur nunc. Donec quis dapibus dui.",
        )

        post2 = Post.objects.create(
            title="sample post 2",
            body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sollicitudin tristique semper. Nulla porttitor lorem leo, ut ornare leo lobortis ut. Phasellus ut finibus purus. In elementum a nibh nec cursus. Donec et nisl non mi mattis auctor. Praesent sit amet gravida nisl, vitae pulvinar diam. Duis vel pulvinar dui. Aenean a purus metus. Morbi et volutpat nulla, at congue ligula. Fusce tristique turpis vitae tincidunt ullamcorper. Sed vestibulum eros quis justo faucibus malesuada. Phasellus a eros venenatis, eleifend ex in, efficitur nunc. Donec quis dapibus dui.",
        )

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
        self.post = Post.objects.create(
            title='Learn JavaScript in this 23 hour course',
            body='this is a beginner course on JS'
        )

    def test_detail_page_returns_correct_response(self):
        response=self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html')

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertContains(response, self.post.created_at)