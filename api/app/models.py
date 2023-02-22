from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    matricule = models.IntegerField()
    registerDate = models.DateTimeField(auto_now=True)


class Email(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Password(models.Model):
    password = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Phone(models.Model):
    phone = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Picture(models.Model):
    picture = models.FileField(upload_to='pictures')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    date = models.DateTimeField(auto_now=True)
    status = models.TextField()
    type = models.CharField(max_length=8)
    number = models.IntegerField()


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_id = models.IntegerField()
    content_type = models.CharField(max_length=10)  # publication && comment


class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=8)


class PostComment(models.Model):
    date = models.DateTimeField(auto_now=True)
    content_data = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)


class ContentComment(models.Model):
    date = models.DateTimeField(auto_now=True)
    content_data = models.TextField()
    content = models.ForeignKey(Content, on_delete=models.CASCADE)


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)


class VoteNumber(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    number = models.IntegerField()


class Followers(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.IntegerField()


class Booking(models.Model):
    type = models


class Message(models.Model):
    expeditor = models.ForeignKey(User, on_delete=models.CASCADE)
    destinator = models.IntegerField()
    date = models.DateTimeField()