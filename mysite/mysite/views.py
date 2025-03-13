from django.http import HttpResponse

def landing(req):
    return HttpResponse("Hello world!")