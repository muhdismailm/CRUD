from django.contrib.auth import authenticate, login as login
from django.shortcuts import redirect, render
from .models import Students
from django.contrib.auth.models import User


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
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('add_student')

        return render(request, 'login.html', {
            'error': 'Invalid credentials or insufficient permissions.'
        })

    return render(request, 'login.html')

def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{
                'error':'Username already exists.'})
        User.objects.create_superuser(
            username=username,
            password=password)
        return redirect('login')
    return render(request,'register.html')       