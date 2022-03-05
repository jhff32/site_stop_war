from django.shortcuts import render
from .models import Visit
import requests
import json



def home(request):
    #global counter
    ip, user_agent= get_client_ip(request), request.META['HTTP_USER_AGENT']
    location = get_loc_from_ip(ip)
    current_visit = Visit(ip=ip,  user_agent=user_agent, country=location[0],city=location[1])
    if not Visit.objects.filter(ip=ip).exists():
        current_visit.save()
    return render(request, 'stop_war/home.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_loc_from_ip(ip_address:str):
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    location = json.loads(response.content.decode().split("(")[1].strip(")"))
    return location["country_name"], location["city"]

