from rest_framework import generics, permissions

from classes.models import Class
from classes.serializers import ClassSerializer
from classes.permissions import IsOwner

class ClassList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Class.objects.filter(user=self.request.user)
        
    serializer_class = ClassSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (IsOwner,)