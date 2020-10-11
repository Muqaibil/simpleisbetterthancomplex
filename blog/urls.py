from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>', views.post_detail, name='blog_detail'),
    path('<int:post_id>/edit', views.Edit_Post, name='edit_post'),
    path('/new', views.New_Post, name='new_post'),
]