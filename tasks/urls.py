from django.urls import path
from . import views
app_name = "tasks"

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_task, name="add"),
    path('update/<int:id>/', views.update_task, name="update"),
]
