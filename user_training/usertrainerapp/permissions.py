from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name = 'Admin').exixts()
    
class IsTeamLead(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name = 'Team_Leader').exixts()

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name = 'User').exixts()        