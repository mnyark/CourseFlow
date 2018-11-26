from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey
from .utils import color_hash_from_name
from django.contrib.auth.models import User

class Node(MPTTModel):
	# parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	# course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='+')
	# concentration = models.ForeignKey('Concentration',on_delete=models.CASCADE, related_name='concentration')

	# def __str__(self):
	# 	return f'Node({self.course})'
	...

class Course(models.Model):
	code = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField()
	color = models.CharField(max_length=100, blank=True)
	credit_hours = models.IntegerField()
	# prereqs = models.ManyToManyField('Course', blank=True)
	concurrent_enrollment = models.ForeignKey('Course', blank=True, null=True, on_delete=models.CASCADE, related_name='+')
	key = models.AutoField(primary_key=True)
	SPRING = 'S'
	FALL = 'F'
	BOTH = 'B'
	choices  = (
		(SPRING, 'Spring'),
		(FALL, 'Fall'),
		(BOTH, 'Both')
		)
	semester = models.TextField(choices=choices, max_length=2, default=FALL)


	def save(self, *args, **kwargs):
		self.color = color_hash_from_name(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return f'{self.code} - {self.title}'


class Concentration(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.name}'

class Major(models.Model):
	name = models.CharField(max_length=100)


	def __str__(self):
		return f'{self.name}'

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete=models.PROTECT)
	concentration = models.ForeignKey(Concentration, related_name="+",on_delete=models.PROTECT, blank=True, null=True)
	courses_taken = models.ManyToManyField(Course, related_name="+", blank=True)
	major = models.ForeignKey(Major, related_name="+", on_delete=models.PROTECT, blank=True, null=True)
	first_time_logged_in = models.BooleanField(default=True)

	def __str__(self):
		return f'UserProfile({self.user.username})'

def create_user_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_user_profile, sender=User)
