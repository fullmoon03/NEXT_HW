from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Article, Comment

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        exist_user = User.objects.filter(username=username)

        if exist_user:
            error = "이미 존재하는 유저입니다."
            return render(request, 'registration/signup.html', {'error': error})
        
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        
        return redirect('home')
    
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
            return redirect(request.GET.get('next', '/'))

        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, 'registration/login.html', {'error': error})
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return redirect('list')

@login_required(login_url="/registration/login/")
def new(request):
    if request.method == 'POST':
        
        article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
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

@login_required(login_url="/registration/login/")
def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            content = request.POST['content'],
            author = request.user,
        )
        return redirect('detail', article_id)
    return render(request, 'detail.html', {'article': article})

def reply_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    Comment.objects.create(
        article = comment.article,
        content = request.POST['content'],
        author = request.user,
        parent_comment = comment,
    )
    return redirect('detail', comment.article.id)

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        Article.objects.filter(id=article_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
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

