    
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
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