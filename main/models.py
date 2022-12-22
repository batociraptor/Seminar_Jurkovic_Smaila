from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=30, verbose_name="Last name")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of birth")
    location = models.CharField(max_length=40, verbose_name="User location")
    email = models.EmailField()

    def __str__(self):
        return self.last_name


class Profile(models.Model):
    profile_name = models.CharField(max_length=30, verbose_name="Profile name")
    profile_owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Profile owner")
    date_created = models.DateField(null=True, blank=True, verbose_name="Date created")
    avatar = models.ImageField(verbose_name="Profile avatar")
    description = models.TextField(max_length=50, verbose_name="Profile description")
    followers = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.profile_name


class Like(models.Model):
    like_id = models.CharField(max_length=20, verbose_name="Like ID")
    user_like = models.ForeignKey('Profile', on_delete=models.CASCADE, default=1, verbose_name="Like by")
    time_liked = models.DateField(null=True, blank=True, verbose_name="Time of liking")

    def __str__(self):
        return self.like_id


class Comment(models.Model):
    comment_id = models.CharField(max_length=13, verbose_name="Comment ID")
    content = models.TextField(max_length=50, verbose_name="Content")
    user_comment = models.ForeignKey('Profile', on_delete=models.CASCADE, default=1, verbose_name="Commented by")
    time_commented = models.DateField(null=True, blank=True, verbose_name="Time of commenting")

    def __str__(self):
        return self.comment_id


class Post(models.Model):
    post_id = models.CharField(max_length=14, verbose_name="Post ID")
    content = models.CharField(max_length=300, verbose_name="Content")
    created_by = models.ForeignKey('Profile', on_delete=models.CASCADE, default=1, verbose_name="Created by")
    time_posted = models.DateField(null=True, blank=True, verbose_name="Time of posting")
    likes = models.ManyToManyField(Like, verbose_name="Liked by")
    comments = models.ManyToManyField(Comment, verbose_name="Comments")
    

    def __str__(self):
        return self.post_id