from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")


def aboutUs(request):
    return HttpResponse("Welcome to first Django app...")