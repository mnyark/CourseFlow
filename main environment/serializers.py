from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'code', 'title', 'description', 'credit_hours', 'prereqs', 'concurrent_enrollment',)