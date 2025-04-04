from rest_framework import permissions


class CheckOwner( permissions.BasePermission ):
    def has_permission(self, request, view):
        if request.user.role == 'преподователь':
            return True
        return False


class CheckUserReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'клиент':
            return True
        return False



class CheckCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by.id == request.user.id