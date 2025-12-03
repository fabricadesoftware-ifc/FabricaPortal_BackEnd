from rest_framework.permissions import BasePermission, SAFE_METHODS
import os
#import jwt
#from jwt.exceptions import InvalidTokenError

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

class EspTagPermission(BasePermission):
     def has_permission(self, request, view):
        token = request.headers.get("X-ESP-TOKEN")
        secret = os.getenv("ESP_SECRET_TOKEN")
        if not token:
            return False
        return bool(token == secret)
        #try:
            #payload = jwt.decode(token, secret, algorithms=["HS256"])
        #except InvalidTokenError:
            #return False