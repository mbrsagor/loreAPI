from django.shortcuts import render, get_object_or_404
from .models import Student
from .serializers import (
    StudentSerializer,
    DetailStudentSeriliazer
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework import status


class APIListView(ListAPIView):
    queryset         = Student.objects.all()
    serializer_class = StudentSerializer


class CreateApiView(CreateAPIView):
    queryset         = Student.objects.all()
    serializer_class = StudentSerializer


class DetailAPIView(RetrieveAPIView):
    queryset         = Student.objects.all()
    serializer_class = DetailStudentSeriliazer
    lookup_field     = 'id'


class UpdateAPIView(RetrieveUpdateAPIView):
    queryset         = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field     = 'id'


class DeleteAPIView(DestroyAPIView):
    queryset         = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field     = 'id'

    def delete(self, request, id):
        delete = get_object_or_404(Student, id=id)
        delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

