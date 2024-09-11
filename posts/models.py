from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_image', null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} {self.owner}'






    
