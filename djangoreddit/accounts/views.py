from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/home.html')

        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords didn\'t match'})
        return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')

def home(request):
    return render(request, 'accounts/home.html')
