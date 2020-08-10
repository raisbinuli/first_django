from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Muh Rais',
        'title':'Blog Post 1',
        'content': 'First blog content',
        'date_posted': 'August 08, 2020'
    },
    {
        'author': 'Budi Lestarie',
        'title':'Blog Post 2',
        'content': 'Second blog content',
        'date_posted': 'August 08, 2020'
    }
]


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
