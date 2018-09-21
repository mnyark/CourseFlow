from django.db import models

class Course(models.Model):
	code = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField()
	credit_hours = models.IntegerField()
	prereqs = models.ManyToManyField('Course', blank=True)
	concurrent_enrollment = models.ForeignKey('Course', blank=True, null=True, on_delete=models.CASCADE, related_name='+')

	def __str__(self):
		return f'{self.code} - {self.title}'