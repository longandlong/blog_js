from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Article


class ArticleMethodTests(TestCase):
	
	def test_was_published_recently_with_futher_article(self):
		
		time = timezone.now() + datetime.timedelta(days=30)
		futher_article = Article(pub_date=time)
		self.assertEqual(futher_article.was_published_recently(),False)
# Create your tests here.
