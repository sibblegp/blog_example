__author__ = 'gsibble'

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from gs_blog import views

urlpatterns = patterns('',

    #/blog/
    url(r'^$', views.BlogPostListView.as_view(), name='index'),

    #/blog/5/
    url(r'^posts/(?P<pk>\d+)/$', views.BlogPostDetailView.as_view(), name='detail'),

    #/blog/author/
    url(r'^author/$', TemplateView.as_view(template_name='gs_blog/author.html'), name='author'),

    #/blog/submit/
    url(r'^submit/$', views.CreateBlogPostView, name='submit'),

    #/polls/5/delete/
    url(r'^posts/(?P<post_id>\d+)/delete/$', views.DeleteBlogPostView, name='delete'),
)