from django.shortcuts import render, redirect
from .models import UserManager, User

def index(request):
    return render(request, 'logreg/index.html')

def register(request):
    if request.method == 'POST':
        ninja_data = request.POST
        errors = User.objects.validate(ninja_data)
        if not errors:
            user = User.objects.create(
                fname = ninja_data['fname'],
                lname = ninja_data['lname'],
                email = ninja_data['email'],
                pword = ninja_data['pword'])
            request.session['ninja'] = user.id
            print user.lname
            print user.id
            return redirect('/success')
    print errors
    return redirect('/')

def login(request):
    if request.method == 'POST':
        ninja_data = request.POST
    return redirect('/')

def success(request):
    return render(request, 'logreg/index.html')
