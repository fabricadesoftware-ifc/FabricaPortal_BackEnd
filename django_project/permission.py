from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomGeneralPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_verified)
    

class UserCustomPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_verified)
    
    
class VerifyCustomPermission(BasePermission):
    
        def has_permission(self, request, view):
            return bool(request.user and request.user.is_authenticated and request.user.is_verified)
