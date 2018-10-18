from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def index(request):
    context = {'all_courses': Course.objects.all()}
    return render(request, 'courseapp/index.html', context)

def add(request):
    if request.method == "POST":
        errors = {}
        
        if len(request.POST['name']) == 0:
            errors['name'] = "You must enter a name"
        elif len(request.POST['name'])<5:
            errors['name'] = "Name must be greater than 5 characters"
        
        if len(request.POST['description'])==0:
            errors['description'] = "You must enter a description"
        elif len(request.POST['description'])<15:
            errors['description'] = "Description must be greater than 15 characters."
        
        print(errors)
        if len(errors):
            for key,value in errors.items():
                messages.error(request, value)
        else:
            Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        print(request.POST)
    return redirect('/')

def destroy(request, course_id):
    content={
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'courseapp/destroy.html', content)

def confirm(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')
