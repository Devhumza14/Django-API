from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Student, Program
from .serializers import StudentSerializer, ProgramSerializer

class ProgramViewset(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    # Changed from IsAuthenticated to AllowAny
    permission_classes = [permissions.AllowAny] 

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Changed from IsAuthenticated to AllowAny
    permission_classes = [permissions.AllowAny]