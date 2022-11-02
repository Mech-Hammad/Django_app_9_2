from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, TemplateView, ListView

# Create your views here.

class BlogView(DetailView):
    model = Post
    template_name = 'blog/blog.html'

class HomeView(ListView):
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(status=1).order_by('-date_created')

class AboutView(TemplateView):
    template_name = 'blog/about.html'