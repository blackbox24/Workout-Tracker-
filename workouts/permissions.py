from rest_framework import permissions


class IsWorkoutOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a workout to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # obj is the Workout instance
        # Assumes your Workout model has a 'user' field (which contains the ID)
        return obj.user == request.user
