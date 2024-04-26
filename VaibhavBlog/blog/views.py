from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    # return HttpResponse("Hi")
    # load all the post from db(10)
    posts=Post.objects.all()[:11]
    #(posts)
    data = {
        'posts': posts
    }

    return render(request,'home.html',data)