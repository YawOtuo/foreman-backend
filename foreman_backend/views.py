from django.http import HttpResponse

def home(request):
    return HttpResponse("Server is up and running")
