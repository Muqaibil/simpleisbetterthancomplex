from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

'''
    URL --> View [models + templates] view is a middle man between URL and models. 
    it capture the data from model, render it and pass it to the url (templates)
'''

def all_posts(request):
    all_posts = Post.objects.all()
    return render(request,'blog/all_posts.html', {'posts':all_posts})

'''
any view should return something

render must take the request, html path, funcitons actual name and html name to use it in templates
'''



def post_detail(request, post_id):
    single_post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post_detail':single_post})


def New_Post(request):
    form = PostForm()
    return render(request, 'blog/new_post.html', {'form':form})
    pass



def Post_Edit(request):
    pass

