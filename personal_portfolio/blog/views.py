from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    total_blogs = Blog.objects.count
    all_blogs_fields = Blog.objects.order_by('-date')[:5] # recent top 5
    context = {
        'all_blogs_fields': all_blogs_fields, 
        'total': total_blogs
    }
    return render(request, 'pages/all_blogs.html', context)

def about(request):
    return render(request, 'pages/about.html')

def details(request, blog_id):
    # Get the blog from the table Blog, where the primary key or id is equal to blog_id
    # Eg. /blog/1, /blog/20
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'pages/detail.html', {'blog':blog})
