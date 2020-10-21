from django.shortcuts import render
from django.http import HttpResponse

from .extra import get_client_ip

def home_view(request):
    context = {
    'title' : "Home",
    'ip'    : get_client_ip(request)

    }


    return render(request, 'home.html', context)


def about_view(request):
    context = ({
        'title'  : "About",

    })


    return render(request, 'about.html', context)
