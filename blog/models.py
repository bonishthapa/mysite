from django.db import models
from django.conf import settings



# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/user')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=20)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null= True, blank= True, related_name='comments')

    def __str__(self):
        return self.author


