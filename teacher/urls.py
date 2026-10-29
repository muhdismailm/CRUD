from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student<int:student_id>/', views.update_student, name='edit_student'),
    path('delete_student<int:student_id>/', views.delete_student, name='delete_student'),
    path('login/', views.login_view, name='login'),
]