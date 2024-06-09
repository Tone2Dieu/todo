from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.DetailTodo.as_view(), name="todo_detail"),
    path("", views.ListTodo.as_view(), name="todo_list")
]