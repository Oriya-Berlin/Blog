from django.urls import path

from . import views


# blog/
urlpatterns = [
    path('', views.home, name='blog-home-page'),  # master
    path('about/', views.about, name='blog-about-page'),
]


