from rest_framework import permissions

class ProfilePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return True