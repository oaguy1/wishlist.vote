from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from .models import ListItem, Wishlist
from .permissions import IsCreatorOrReadOnly
from .serializers import ListItemSerializer, UserSerializer, GroupSerializer, WishlistDetailSerializer, WishlistSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoints that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoints that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WishlistViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows CRUD on lists
    """
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return WishlistSerializer
        else:
            return WishlistDetailSerializer


class ListItemViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows CRUD on list items
    """
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]