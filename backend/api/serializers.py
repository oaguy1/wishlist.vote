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
    class Meta:
        model = ListItem
        fields = ['url', 'name', 'description', 'wishlist', 'created_by', 'created_at', 'updated_at']


class WishlistDetailSerializer(serializers.HyperlinkedModelSerializer):
    list_items = ListItemSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ['url', 'slug', 'name', 'description', 'created_by', 'created_at', 'updated_at', 'list_items']

