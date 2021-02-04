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
    can_upvote = serializers.SerializerMethodField()

    def get_upvote_count(self, obj: dict):
        return Upvote.objects.filter(list_item=obj.id).count()

    def get_can_upvote(self, obj: dict):
        # https://stackoverflow.com/questions/27934822/get-current-user-in-model-serializer
        request = self.context.get('request', None)

        if request and request.user.id:
            return Upvote.objects.filter(list_item=obj.id, user=request.user.id).count() == 0
        else:
            return False

    
    class Meta:
        model = ListItem
        fields = ['url', 'name', 'description', 'wishlist', 'created_by', 'created_at', 'updated_at', 'upvote_count', 'can_upvote']


class WishlistDetailSerializer(serializers.HyperlinkedModelSerializer):
    list_items = ListItemSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ['url', 'slug', 'name', 'description', 'created_by', 'created_at', 'updated_at', 'list_items']

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ['user', 'list_item']