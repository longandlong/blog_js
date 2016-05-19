from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Article, Photo
from django.template import loader

def index(request):
	Latest_articles = Article.objects.order_by('-pub_date')[:2]
	template = loader.get_template('blog/index.html')
	return HttpResponse(template.render(request))


def details(request, article_id):
	blog_detail = Article.objects.get(id=article_id)
	#template = loader.get_template('blog/blog_details.html')
	#return HttpResponse("Here are the details and the name of the article is %s" % article_name)
	return render_to_response('blog/blog_details.html', {'blog_detail':blog_detail})

def photos(request):
	template = loader.get_template('blog/3/0/index.html')
	return HttpResponse(template.render())

def blogs(request):
	blog_list = Article.objects.order_by('-pub_date')[:10]
	#template = loader.get_template('blog/blogs.html')
	#return HttpResponse(template.render({'blog_list':blog_list}, request))
	return render_to_response('blog/blogs.html', {'blog_list':blog_list})	

def friends(request):
	template = loader.get_template('blog/friends.html')
	return HttpResponse(template.render())


def hobbies(request):
	return HttpResponse('Hobbies here...')

def favorites(request):
	return HttpResponse('Favorites here...')

def forum(request):
	return HttpResponse('Forum here...')

def groups(request):
	return HttpResponse('Groups here...')

def events(request):
	return HttpResponse('Events here...')

def myspacetv(request):
	return HttpResponse('MySpaceTV here...')


def navBlog(request,navBlogValue):
	nav = {'life':'LF','python':'PY','feelings':'FL','javascript':'JS','php':'PH','tools':'TL'}
	life = 'LF'
	python = 'PY'
	feelings = 'FL'
	javascript = 'JS'
	php = 'PH'
	tools = 'TL'
	nav_value =Article.objects.filter(class_of_article = nav.get(navBlogValue))
	#return HttpResponse(nav_value[1])
	return render_to_response('blog/blogs.html',{'blog_list':nav_value})


def music(request):
	return HttpResponse('Music here ... do re me ...')
# Create your views here.
