from rest_framework import generics, permissions

from categories.models import Category
from categories.serializers import CategorySerializer
from categories.permissions import IsOwner

class CategoryList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Category.objects.filter(class_field__user=self.request.user)
        
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     data = dict((k, self.request.data[k]) for k in ('course', 'professor', 'quarter', 'year', 'grade'))

    #     serializer.save(user=self.request.user, **data)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwner,)