from django.urls import path, include
from . import views
from main.views import UserList, ProfileList, LikeList, CommentList, PostList

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user', UserList.as_view()),
    path('profile', ProfileList.as_view()),
    path('like', LikeList.as_view()),
    path('comment', CommentList.as_view()),
    path('post', PostList.as_view()),
]