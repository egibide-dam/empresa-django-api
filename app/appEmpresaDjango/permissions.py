from rest_framework import permissions

class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permitir solicitudes GET sin autenticación
        if request.method == 'GET':
            return True
        # Requerir autenticación para otras solicitudes
        return request.user and request.user.is_authenticated

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Allow read-only methods for everyone
            return True
        # Check if the user making the request is the owner of the student object
        return obj.user == request.user

class IsAdmin(permissions.BasePermission):
   def has_permission(self, request, view):
      return request.user.is_admin

class IsEditor(permissions.BasePermission):
   def has_permission(self, request, view):
      return request.user.is_editor

class IsUser(permissions.BasePermission):
   def has_permission(self, request, view):
      return request.user.is_user
