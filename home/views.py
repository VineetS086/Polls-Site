from django.shortcuts import render
from django.http import HttpResponse



def home_view(request):
    context = {
    'title' : "Home",

    }


    return render(request, 'home.html', context)


def about_view(request):
    context = ({
        'title'  : "About",

    })


    return render(request, 'about.html', context)
