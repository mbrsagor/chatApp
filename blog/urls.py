from django.urls import path
from blog import views

urlpatterns = [
    path('category/', views.CategoryCreateListView.as_view()),
    path('articles/', views.ArticleListView.as_view()),
]
