from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_task),
    path('update/<int:id>', views.update_task)
]
