from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Article, Photo
from django.template import loader

def index(request):
	Latest_articles = Article.objects.order_by('-pub_date')[:2]
	template = loader.get_template('blog/index1.html')
	context = {
		'latest_articles': Latest_articles,
	}
	output = ', '.join([q.article_name for q in Latest_articles])
	return HttpResponse(template.render(context,request))


def detail(request, article_name):
	return HttpResponse("Here are the details and the name of the article is %s" % article_name)


def photos(request):
	template = loader.get_template('blog/photos.html')
	return HttpResponse(template.render())

def blogs(request):
	blog_list = Article.objects.order_by('-pub_date')[:5]
	template = loader.get_template('blog/blogs.html')
	#return HttpResponse(template.render({'blog_list':blog_list}, request))
	return render_to_response('blog/blogs.html', {'blog_list':blog_list})	

def friends(request):
	template = loader.get_template('blog/friends.html')
	return HttpResponse(template.render())
# Create your views here.
