from rest_framework import generics, permissions

from classes.models import Class
from classes.serializers import ClassSerializer
from classes.permissions import IsOwner

class ClassList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Class.objects.filter(user=self.request.user)
        
    serializer_class = ClassSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        data = dict((k, self.request.data[k]) for k in ('course', 'professor', 'quarter', 'year', 'grade'))

        serializer.save(user=self.request.user, **data)

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsOwner,)