from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
@python_2_unicode_compatible
class Article(models.Model):

	article_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('data publised')

	def __str__(self):
		return self.article_name

	def was_published_recently(self):
		return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


@python_2_unicode_compatible
class Comments(models.Model):

	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	comments_text = models.CharField(max_length=200)

	def __str__(self):
		return self.comments_text