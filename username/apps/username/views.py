from django.shortcuts import render, redirect
from .models import UserManager, User

# Create your views here.
def index(request):
    if 'ninja' not in request.session:
        request.session['ninja'] = 'unregistered'
        request.session['fail'] = ''
    ninja_data = {
        'ninja' : request.session['ninja'],
        'fail' : request.session['fail']
        }
    return render(request, 'username/index.html', ninja_data)

def add_username(request):
    if request.method == 'POST':
        errors = User.objects.validate(request.POST)
        if not errors:
            username = request.POST['username']
            request.session['ninja'] = username
            user = User.objects.create(user_name=username)
            return redirect('/success')
        else:
            request.session['fail'] = request.POST['username']
            return redirect('/')

def success(request):
    users = User.objects.all()
    ninja_data = {
        'ninja_name' : request.session['ninja'],
        'ninjas' : users
        }
    return render(request, 'username/success.html', ninja_data)
