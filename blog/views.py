from django.shortcuts import render
from . models import Post

# Create your views here.

'''
    URL --> View [models + templates] view is a middle man between URL and models. 
    it capture the data from model, render it and pass it to the url (templates)
'''

def all_posts(request):
    all_posts = models.Post.objects.all()
    return render(request,'blog/all_posts.html',{'posts':all_posts})

'''
any view should return something

render must take the request, html path, funcitons actual name and html name to use it in templates
'''



def post_detail(request, post_id):
    pass