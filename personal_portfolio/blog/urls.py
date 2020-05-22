from django.urls import path, include
from django.conf import settings

from . import views

app_name = 'blog'

# all_blogs which renders pages/all_blogs.html, is available as blog:all_blogs
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.details, name='details')
]