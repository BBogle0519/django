from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Step', views.StepCountViewSet, basename="Step")

urlpatterns = [
    path('', include(router.urls)),
]
