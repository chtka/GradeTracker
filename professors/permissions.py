from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return (
            request.user.username and
            (request.method in permissions.SAFE_METHODS or 
            request.user.is_staff)
        )