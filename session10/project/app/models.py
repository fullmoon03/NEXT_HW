from django.db import models


class Post(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()
#comment
#on_delete
# >casecade 코멘트는 포스트에 종속적 : 포스트가 사라지면 코멘트도 사라짐
   def __str__(self):
       return self.title
   

class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()


   def __str__(self):
       return self.content
