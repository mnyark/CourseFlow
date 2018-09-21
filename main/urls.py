from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)

# urlpatterns = [
#     path('data', views.data),
#     path('', views.index)
# ]

urlpatterns = router.urls