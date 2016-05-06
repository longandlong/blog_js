from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


# Create your models here.
@python_2_unicode_compatible
class Article(models.Model):

	article_name = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('data publised')

	def __str__(self):
		return self.article_name

	def was_published_recently(self):
		return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def digest(self):
		return self.body[:100]

@python_2_unicode_compatible
class Comment(models.Model):

	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	comments_text = models.CharField(max_length=200)

	def __str__(self):
		return self.comments_text


class Photo(models.Model):
	photo_name = models.CharField(max_length=200)
	photo_path = models.CharField(max_length=200)
	
	def __str__(self):
		return self.photo_name


class Blog(models.Model):
	blogs_number = models.IntegerField(default=0)
	
	def __str__(self):
		return self.blogs_number
	

















