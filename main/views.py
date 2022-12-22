from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import User, Profile, Like, Comment, Post

def homepage(request):
    return render(request, "base.html")

class UserList(ListView):
    model = User

class ProfileList(ListView):
    model = Profile

class LikeList(ListView):
    model = Like

class CommentList(ListView):
    model = Comment

class PostList(ListView):
    model = Post