from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import redirect, render
from .models import Students


def index(request):
    std = Students.objects.all()
    return render(request, 'index.html', {'student': std})


def add_student(request):

    if request.method == "POST":
        name = request.POST.get('name')
        course = request.POST.get('course')
        age = request.POST.get('age')

        Students.objects.create(
            name=name,
            course=course,
            age=age
        )

        return redirect('index')

    return render(request, 'add_student.html')

def update_student(request,student_id):
    std=Students.objects.get(id=student_id)
    if request.method=="POST":
        std.name=request.POST.get('name')
        std.course=request.POST.get('course')
        std.age=request.POST.get('age')
        std.save()
        return redirect('index')
    return render(request,'edit_student.html',{'student':std})
    
def delete_student(request,student_id):
    std=Students.objects.get(id=student_id)
    std.delete()
    return redirect('index')