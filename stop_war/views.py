from django.shortcuts import render


def home(request):
    return render(request, 'stop_war/home.html')
