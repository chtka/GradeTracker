from django_filters import rest_framework as filters

from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from professors.models import Professor
from professors.serializers import ProfessorSerializer
from professors.permissions import IsAdminUserOrReadOnly

class ProfessorFilter(filters.FilterSet):

    class Meta:
        model = Professor
        fields = ['first_name', 'last_name',]

class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProfessorFilter

class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)