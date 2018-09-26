from rest_framework.serializers import ModelSerializer
from .models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model  = Student
        fields = ('__all__')



class DetailStudentSeriliazer(ModelSerializer):
    class Meta:
        model  = Student
        fields = 'name', 'roll'
