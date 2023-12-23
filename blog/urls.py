from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.BlogPost.as_view(), name='blog_post'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='post_like'),
    path('post/add/', views.CreatePost.as_view(), name="add_post"),
    path('<slug:slug>/update/', views.UpdatePost.as_view(),
         name='update_post'),
]
