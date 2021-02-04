from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import ListItem, Upvote, Wishlist

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['url', 'slug', 'name', 'description', 'created_by', 'created_at', 'updated_at']


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    upvote_count = serializers.SerializerMethodField()

    def get_upvote_count(self, obj):
        return Upvote.objects.filter(list_item=obj.id).count()

    
    class Meta:
        model = ListItem
        fields = ['url', 'name', 'description', 'wishlist', 'created_by', 'created_at', 'updated_at', 'upvote_count']


class WishlistDetailSerializer(serializers.HyperlinkedModelSerializer):
    list_items = ListItemSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ['url', 'slug', 'name', 'description', 'created_by', 'created_at', 'updated_at', 'list_items']

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ['user', 'list_item']