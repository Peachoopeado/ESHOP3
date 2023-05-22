from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.open_main, name='main'),
    path('news/', views.news_list, name='news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
]
