"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('list/', views.list, name='list'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('update/<int:article_id>/', views.update, name='update'),
    path('delete/<int:article_id>/', views.delete, name='delete'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('reply-comment/<int:comment_id>', views.reply_comment, name='reply-comment'),
    path('delete-comment/<int:article_id>/<int:comment_id>', views.delete_comment, name='delete-comment'),
]
