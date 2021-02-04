from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets, status
from rest_framework import response
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import ListItem, Upvote, Wishlist
from .permissions import IsCreatorOrReadOnly
from .serializers import ListItemSerializer, UpvoteSerializer, UserSerializer, GroupSerializer
from .serializers import WishlistDetailSerializer, WishlistSerializer


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

    @action(detail=True, methods=['post'])
    def upvote(self, request: Request, pk: int = None):
        upvote_data = {
            'user': request.user.id, 
            'list_item': self.get_object().id
        }
        upvote = UpvoteSerializer(data=upvote_data)
            
        if upvote.is_valid():
            upvote.save()
            return Response({'status': 'created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(upvote.errors, status.HTTP_400_BAD_REQUEST)