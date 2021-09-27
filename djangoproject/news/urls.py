from django.urls import path
from . import views

# <int:pk> - динамический параметр, благодаря которому мы сможем просматривать каждую новость на новой странице
# и вызываем классв конце которого обязательно обращаемся к методу as_view()
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
]
