from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.

def home(request):
    return redirect('list')

def new(request):
    if request.method == 'POST':
        
        article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('detail', article.id)
    return render(request,'new.html')

def list(request):

    articles = Article.objects.all()
    # return render(request,'list.html', {'articles': articles})
    # categories = Category.objects.all()
    categories = []
    num_articles = []
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)
    for temp_ct in categories:
        articles = Article.objects.filter(category = temp_ct)
        num_articles.append(len(articles))
    
    list = zip(categories, num_articles)
    

    return render(request, 'list.html', {'list': list})

def category(request, category_name):
    articles = Article.objects.filter(category = category_name)
    return render(request,'category.html', {'articles': articles, 'category_name': category_name})
    
    # 왜 얘는 안 됨?
    # return render(request,'category.html', {'articles': articles}, {'category_name': category_name})


# def detail(request, article_id):
#     article = Article.objects.get(id=article_id)
#     if request.method == 'POST':
#         Comment.objects.create(
#             article = article,
#             content = request.POST['content']
#         )
#         return redirect('detail', article_id)
#     return render(request, 'detail.html', {'article': article})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            content = request.POST['content'],
        )
        return redirect('detail', article_id)
    return render(request, 'detail.html', {'article': article})

def reply_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    Comment.objects.create(
        article = comment.article,
        content = request.POST['content'],
        parent_comment = comment,
    )
    return redirect('detail', comment.article.id)

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        Article.objects.filter(id=article_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('detail', article_id)
    return render(request,'update.html', {'article': article})



def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('home')

def delete_comment(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    # print(comment.article.id, comment.article, comment.article.content)
    comment.delete()
    return redirect('detail', article_id)

