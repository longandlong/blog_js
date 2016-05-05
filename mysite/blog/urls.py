from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^photos/$', views.photos, name = 'photos'),
	url(r'^blogs/$', views.blogs, name = 'blogs'),
	url(r'^friends/$', views.friends, name = 'friends'),
	url(r'^hobbies/$', views.hobbies, name = 'hobbies'),
	url(r'^favorites/$', views.favorites, name = 'favorites'),
	url(r'^forum/$', views.forum, name = 'forum'),
	url(r'^groups/$', views.groups, name = 'groups'),
	url(r'^events/$', views.events, name = 'events'),
	url(r'^myspacetv/$', views.myspacetv, name = 'myspacetv'),
	url(r'^comedy/$', views.comedy, name = 'comedy'),
	url(r'^classfields/$', views.classfields, name = 'classfields'),
	url(r'^music/$', views.music, name = 'music'),
	url(r'^blogs/(.*?)/$',views.navBlog,name = 'navBlog'),
]
