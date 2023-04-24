from rest_framework.permissions import BasePermission





class IsStudentUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_student)


class IsInstructortUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_instructor)



  