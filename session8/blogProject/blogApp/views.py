from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST, '------') # 터미널에서 데이터 확인

        Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('list')
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
    print({'category_name': category_name})
    return render(request,'category.html', {'articles': articles, 'category_name': category_name})
    
    # 왜 얘는 안 됨?
    # return render(request,'category.html', {'articles': articles}, {'category_name': category_name})


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})