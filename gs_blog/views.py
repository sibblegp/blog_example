from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from gs_blog.models import BlogPost

import datetime
# Create your views here.

class BlogPostListView(generic.ListView):
    template_name = 'gs_blog/index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return BlogPost.objects.order_by('-publish_datetime')

class BlogPostDetailView(generic.DetailView):
    template_name = 'gs_blog/post.html'
    model = BlogPost
    context_object_name = 'post'

def CreateBlogPostView(request):
    post_title = request.POST['postTitle']
    post_text = request.POST['postText']

    post = BlogPost()
    post.post_title = post_title
    post.post_text = post_text
    post.publish_datetime = datetime.datetime.now()

    post.save()

    return redirect('gs_blog:detail', pk=post.id)

def DeleteBlogPostView(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    return redirect('gs_blog:index')