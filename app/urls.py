from django.urls import path
from .views import PostLIstView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


# blog/
urlpatterns = [
    #path('', views.home, name='blog-home-page'),  # master
    path('', PostLIstView.as_view(), name='blog-home-page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about-page'),
]


