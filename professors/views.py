from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from professors.models import Professor
from professors.serializers import ProfessorSerializer
from professors.permissions import IsAdminUserOrReadOnly

class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)

class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = (IsAdminUserOrReadOnly,)