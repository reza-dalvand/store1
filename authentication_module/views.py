from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, './authentication/signin_signup.html', {})


def register(request):
    return render(request, './authentication/signup.html', {})
