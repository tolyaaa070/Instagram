from .models import (UserProfile, Follow,Save,SaveItem,
                     Post, PostLike,CommentLike,Story,Comment)
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username' , 'last_name', 'first_name',
                  'bio' , 'image' , 'website']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username' ]

class FollowSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%y , %H:%M')
    class Meta:
        model = Follow
        fields = ['follower' , 'following' , 'created_at']
class CommentSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    created_at = serializers.DateTimeField(format='%d-%m-%y , %H:%M')

    class Meta:
        model = Comment
        fields = ['post','user','text','parent','created_at']

class ComSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Comment
        fields = ['user','text']


class CommentLikeSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%y , %H:%M')

    class Meta:
        model = CommentLike
        fields = ['user', 'comment' , 'like', 'created_at']

class PostListSerializers(serializers.ModelSerializer):
    user= UserSerializers()
    class Meta:
        model = Post
        fields = ['user','image','video']


class PostDetailSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    comment = ComSerializers(read_only=True, many=True)
    created_at = serializers.DateTimeField(format='%d-%m-%y , %H:%M')

    class Meta:
        model = Post
        fields = ['user' , 'comment','image','video',
                  'description' ,'hashtag','created_at']

class PostLikeSerializers(serializers.ModelSerializer):
    post = PostListSerializers()
    created_at = serializers.DateTimeField(format='%d-%m-%y , %H:%M')

    class Meta:
        model = PostLike
        fields = ['user' , 'post','like','created_at']



class StorySerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%y ')
    user = UserSerializers()
    class Meta:
        model = Story
        fields = ['user', 'image', 'video','created_at']
class SaveSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Save
        fields = ['user']

class SaveItemSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%y , %H:%M')

    class Meta:
        model = SaveItem
        fields = ['post','save', 'created_at']
