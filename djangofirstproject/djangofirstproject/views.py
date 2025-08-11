from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     data = {
#         'title':'Home Page',
#         'rishi':"Welcome to rishi app",
#         # 'list' : ['Java', 'python', "Django", 'spring'],
#         'numbers' : [10,30,50,70,80,100],
#         'student_details':[
#             {'name':'Rishi singh','phone':7800017055},
#             {'name':'Saloni','phone':7725885515},
#         ]
#     }
#     return render(request, "index.html", data)

def home(request):
    return render(request, "home.html")


def movies(request):
    return render(request, "movies.html")

def theatres(request):
    return render(request, "theatres.html")

def booking(request):
    return render(request, "booking.html")

def signup_login(request):
    return render(request, "signup_login.html")

# def home(request):
#     return render(request, "index.html")


# def aboutUs(request):
#     return HttpResponse("Welcome to first Django app...")

# def course(request):
#     return HttpResponse("Welcome to Rishi Code")

# def courseDetails(request, courseid):
#     return HttpResponse(courseid)