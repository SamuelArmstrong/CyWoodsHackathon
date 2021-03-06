from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import  ParseError
from .serializers import PersonSerializer, SchoolSerializer
from .models import Person, School


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    @action(methods=['get'], detail=True)
    def get_students(self, request, pk=None):
        students = Person.objects.filter(school=get_object_or_404(School, pk=pk))
        serializer = PersonSerializer(students, many=True)
        return Response(serializer.data)
    @action(methods=['get'], detail=False)
    def get_small_schools(self, request):
        small_schools = [i for i in School.objects.all() if School.size(i) < 3]
        serializer = SchoolSerializer(small_schools, many=True)
        return Response(serializer.data)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(methods=['get'], detail=False)
    def get_student_by_name(self, request):
        name = request.query_params.get('name', None)
        if name is not None:
            serializer = PersonSerializer(get_object_or_404(Person, name__iexact=name), many=False)
            return Response(serializer.data)
        else:
            raise ParseError()
