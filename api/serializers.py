from rest_framework import serializers
from accounts.models import Account
from posts.models import Post, Comment, Like


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'email', 'avatar', 'info', 'gender', 'birth_date', 'phone_number', 'subscriptions',
            'subscriptions_count',
            'subscribers_count')
        read_only_fields = ('id', 'phone_number')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'author', 'created_at', 'like_count',)
        read_only_fields = ('id', 'like_count',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text',)
        read_only_fields = ('id')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at',)
        read_only_fields = ('id', 'created_at',)
