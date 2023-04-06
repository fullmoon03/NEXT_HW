from django.db import models


# Create your models here.
# class Category(models.Model):
#     HOBBY = "hb"
#     FOOD = "fd"
#     PROGRAMMING = "pg"
#     CATEGORY_CHOICES = (
#         (HOBBY, "hobby"),
#         (FOOD, "food"),
#         (PROGRAMMING, "programming"),
#     )
#     name = models.CharField(
#         choices=CATEGORY_CHOICES,
#         max_length=2,
#         default=PROGRAMMING,
#     )

#     def __str__(self):
#         return self.name

class Article(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
