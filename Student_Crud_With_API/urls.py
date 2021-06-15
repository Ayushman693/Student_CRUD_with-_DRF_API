from django.contrib import admin
from django.urls import path, include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name = "addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('api/', include('enroll.API.urls')),
    ]
