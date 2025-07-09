from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='user_image/' , null=True , blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.username},{self.last_name},{self.first_name},{self.bio},{self.image},{self.website}'

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE , related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower},{self.following}'

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image_post/', null=True , blank=True)
    video = models.FileField(upload_to='video_post/ ', null=True , blank=True)
    description = models.TextField()
    hashtag =models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'like')

    def __str__(self):
        return f'{self.user},{self.post}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user')
    text = models.TextField()
    parent = models.ForeignKey(UserProfile,on_delete=models.CASCADE , related_name='parent')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post},{self.user} , {self.parent}'

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    like= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'like')


    def __str__(self):
        return f'{self.user},{self.like}'

class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_image/' , null=True , blank=True)
    video = models.FileField(upload_to='story_video/' , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class Save(models.Model):
    user = models.ForeignKey(UserProfile , on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}'


class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    save = models.ForeignKey(Save, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post},{self.save}'
class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='image/', null=True , blank=True)
    video = models.FileField(upload_to='video/', null=True , blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
