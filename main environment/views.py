from django.shortcuts import render
from django.http import JsonResponse
from .models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer

# Create your views here.

def data(request):
	courses = Course.objects.all().values()
	return JsonResponse(list(courses), safe=False)

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


def index(request):
	return render(request, 'index.html')
