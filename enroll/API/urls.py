from django.urls import path, include
from enroll.API import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('crud', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]

