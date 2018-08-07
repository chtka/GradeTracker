from rest_framework import generics, permissions

from assignments.models import Assignment
from assignments.serializers import AssignmentSerializer
from assignments.permissions import IsAssignmentOwner

class AssignmentList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Assignment.objects.filter(category__class_field__user=self.request.user)
        
    serializer_class = AssignmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     data = dict((k, self.request.data[k]) for k in ('course', 'professor', 'quarter', 'year', 'grade'))

    #     serializer.save(user=self.request.user, **data)

class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = (IsAssignmentOwner,)