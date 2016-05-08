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
	LIFE = 'LF'
	PYTHON = 'PY'
	FEELING = 'FL'
	JAVASCRIPT = 'JS'
	PHP = 'PH'
	TOOLS = 'TL'
	
	CLASS_OF_ARTICLE = ((LIFE,'life'),(PYTHON,'python'),(FEELING,'feelings'),(JAVASCRIPT,'Javascript'),(PHP,'php'),(TOOLS,'tools'))
	class_of_article = models.CharField(max_length=2,choices=CLASS_OF_ARTICLE,default=LIFE)
	def __str__(self):
		return self.article_name

	def get_body(self):
		html = self.body.replace('&lt;','<').replace('&gt;','>')
		html = ' '.join(html.split())
		return html
	def was_published_recently(self):
		return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def digest(self):
		html = self.get_body()
		return html[:200]
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
	

















