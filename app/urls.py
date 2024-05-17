from app.views import TodoListAndCreate, TodoDatailChangeAndDelete

from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDatailChangeAndDelete.as_view()),
]