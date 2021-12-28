from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'AIWeb/index.html')


def contact(request):
    return render(request, 'AIWeb/contact.html')


def projects(request):
    return render(request, 'AIWeb/projects.html')


def events(request):
    return render(request, 'AIWeb/events.html')


def academics(request):
    return render(request, 'AIWeb/academics.html')
