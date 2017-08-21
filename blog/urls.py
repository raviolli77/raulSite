from django.conf.urls import url
from . import views	
from .models import Post


urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^blog/', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^contact_page/', views.contact_page, name = 'contact_page'),
	url(r'^cv/', views.cv, name = 'cv'),
]