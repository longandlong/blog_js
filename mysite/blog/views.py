from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
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



# Create your views here.
