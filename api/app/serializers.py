from rest_framework import serializers
from .models import Student, Program

# This turns your Program data into JSON for the market
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

# This turns your Student data into JSON for the market
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'