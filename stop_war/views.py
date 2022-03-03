from django.shortcuts import render
from .models import Visit

counter = 0


def home(request):
    global counter
    ip = get_client_ip(request)
    user_agent = request.META['HTTP_USER_AGENT']
    current_visit = Visit(ip=ip, user_agent=user_agent)
    if not Visit.objects.filter(ip=ip).exists():
        current_visit.save()
        counter = Visit.objects.count()

    return render(request, 'stop_war/home.html', {'counter': counter})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
