from rest_framework import permissions

class IsAssignmentOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.category.class_field.user
    
        