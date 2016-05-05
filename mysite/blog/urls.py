from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<article_name>[0-9]+)/$', views.detail, name='detail'),
	url(r'^photos/$', views.photos, name = 'photos'),
	url(r'^blogs/$', views.blogs, name = 'blogs'),
	url(r'^friends/$', views.friends, name = 'friends'),
]
