from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateTimeField(default=timezone.now)
    # author = next lecture
    content = models.TextField(max_length=3000)
    view_count = models.IntegerField(default=0)
    # tags = net lecture
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'