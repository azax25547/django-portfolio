from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(req):
    blogs = Blog.objects
    return render(req, "blog/blogs.html", {"blogs": blogs})

def detail(req, blog_id):
    detail_data = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'blog/detail.html', {"blog":detail_data})
