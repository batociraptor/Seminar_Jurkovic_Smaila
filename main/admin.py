from django.contrib import admin
from main.models import *

model_list = [User, Profile, Like, Comment, Post]
admin.site.register(model_list)