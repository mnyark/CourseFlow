from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Course, Node, Concentration, Major
from itertools import chain
from django.contrib.auth.models import User

# Create your views here.

def data(request):
	courses = list(Course.objects.all().values())
	conc = get_object_or_404(Concentration, pk=1)
	nodes = Node.objects.filter(concentration=conc)
	graph = []
	for node in nodes:
		children = node.get_children()
		if children is not None:
			children_ids = [child.course.key for child in children]
			graph.append([{"from": node.course.key, "to": child_id} for child_id in children_ids])
	graph = list(chain.from_iterable(graph))
	d = {"courses": courses, "graph": graph}
	return JsonResponse(d, safe=False)

@login_required(login_url='/login')
def index(request):
	user = get_user(request)
	user_profile = user.user
	if user_profile.first_time_logged_in:
		return redirect('/add_courses')
	return render(request, 'index.html')

@login_required
def add_courses(request):
	if request.method == 'GET':
		courses = Course.objects.all()
		ctx = {'courses': courses}
		return render(request, 'courses.html', context=ctx)
	else:
		courses = request.POST.getlist('my-select[]')
		if courses is not None:
			c = Course.objects.filter(code__in=courses)
			user_profile = get_user(request).user
			for i in c:
				user_profile.courses_taken.add(i)
			user_profile.first_time_logged_in = False
			user_profile.save()
		return redirect('/')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return redirect('/')
		else:
			ctx = {"error": "Make sure username and password are correct"}
			return render(request, 'registration/login.html', context=ctx)
	else:
		return render(request, 'registration/login.html')

def register(request):
	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		major = request.POST['major']
		concentration = request.POST['concentration']
		password = request.POST['password']
		user = User.objects.create_user(
			username=email,
			first_name=firstname, last_name=lastname,
			email=email, password=password
			)
		user_profile = user.user
		user_profile.major = Major.objects.get(pk=major)
		user_profile.concentration = Concentration.objects.get(pk=concentration)
		user_profile.save(update_fields=['major', 'concentration'])
		return redirect('/login')
	#get all majors and concentrations
	majors = Major.objects.all()
	concentrations = Concentration.objects.all()
	return render(request, 'registration/register.html', {"majors": majors, "concentrations": concentrations})

@login_required
def semester(request):
	semester = request.GET['semester']
	courses = Course.objects.filter(Q(semester=semester) | Q(semester=Course.BOTH))
	courses_taken = request.user.user.courses_taken.all()
	courses_taken_ids = [c.key for c in courses_taken]
	courses = courses.exclude(key__in=courses_taken_ids)
	return render(request, 'semester.html', {"courses": courses})

@login_required
def profile(request):
	user = request.user
	return render(request, 'profile.html', {'user': user})

@login_required
def logout(request):
	auth_logout(request)
	return redirect('/login')



