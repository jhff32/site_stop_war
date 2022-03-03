from django.shortcuts import render
from django.contrib.gis.utils import GeoIP
from .models import Visit


def home(request):
    ip = get_client_ip(request)
    user_agent = request.META['HTTP_USER_AGENT']
    city = get_city(request)
    Visit(ip=ip, city=city, user_agent=user_agent)

    new_visit = Visit(ip=ip, city=city, user_agent=user_agent)
    new_visit.save()
    counter = Visit.objects.count()

    return render(request, 'stop_war/home.html', {'counter': counter})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_city(request):
    g = GeoIP()
    ip = request.META.get('REMOTE_ADDR', None)
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Russia'  # default city

    return city
