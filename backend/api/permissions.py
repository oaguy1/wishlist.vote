from rest_framework import permissions
from rest_framework.request import Request


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Capture the idea that an object is read-only unless owned  by the current user
    """

    def get_object_permission(self, request: Request, view, obj):
        # Always allow safe methods
        if request.method in permissions.SAFE_METHODS:
            True

        return obj.created_by == request.user
