from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Course, Node, Concentration, UserProfile, Major

# Register your models here.
admin.site.register(Node, MPTTModelAdmin)
models = [Course, Concentration, UserProfile, Major]
for model in models:
	admin.site.register(model)
