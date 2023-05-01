from django.contrib.auth.models import User
from django.db import models




class Article(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    create_date = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null="True", related_name="recomments")

    def __str__(self):
        return self.content
