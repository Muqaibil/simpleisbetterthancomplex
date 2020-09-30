from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts),
    path('<int:post_id>', views.post_detail)
]