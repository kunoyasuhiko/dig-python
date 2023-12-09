from django.test import TestCase
from django.urls import reverse
# from .models import Post
# # Create your tests here.

class IndexUrls(TestCase):
    def test_post(self):
        detail_url = reverse('frontpage')
        response = self.client.post(detail_url)
        self.assertEqual(response.status_code, 200)
