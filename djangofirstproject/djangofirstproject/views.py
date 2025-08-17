from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UsersForm
from service.models import Service


# def home(request):
#     ServiceData = Service.objects.all()
#     for a in ServiceData:
#         print(a.service_icon)
#     print(Service)
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
    # serviceData = Service.objects.all() # all data
    serviceData = Service.objects.all().order_by('service_title') # order by title
    # serviceData = Service.objects.all().order_by('-service_title') # order by title in reverse order
    # serviceData = Service.objects.all().order_by('-service_title')[:2] # order by title in reverse order and limit 2
    # serviceData = Service.objects.all().order_by('-service_title')[2:4] # order by title in reverse order and limit 2
    data = {
        'serviceData' : serviceData
    }
    return render(request, "movies.html", data)

def theatres(request):
    return render(request, "theatres.html")

def booking(request):
    return render(request, "booking.html")

def signup_login(request):
    return render(request, "signup_login.html")

def Thankyou(request):
    if request.method == "GET":
        output  =request.GET.get('output')
    return render(request, "Thankyou.html")

def calculator(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
                    
        except ValueError:
            result = "Invalid input"

    return render(request, "calculator.html", {"result": result})


# Get Method data from form

# def userform(request):
#     finalans = 0
#     try:
#         # n1 = int(request.GET['val1'])
#         # n2 = int(request.GET['val2'])
#         n1 = int(request.GET.get('val1'))
#         n2 = int(request.GET.get('val2'))
#         # print(n1+n2)
#         finalans = n1 + n2
        
#     except:
#         pass
#     return render(request, "userform.html",{'output':finalans})


# Post Method Use  and Redirect 
'''
def userform(request):
    finalans = 0
    data = {}
    try:
        if request.method == "POST":
        # n1 = int(request.GET['val1'])
        # n2 = int(request.GET['val2'])
            n1 = int(request.POST.get('val1'))
            n2 = int(request.POST.get('val2'))
        finalans = n1 + n2
        data = {
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
        
        url = "/thankyou/?output={}".format(finalans)
        return HttpResponseRedirect(url)
        # return HttpResponseRedirect('/thankyou/')
        
    except:
        pass
    # return render(request, "userform.html",{'output':finalans})
    return render(request, "userform.html",data)
'''

def userForm(request):
    submitted_data = None  # Store submitted form data

    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            # Get cleaned form data
            submitted_data = form.cleaned_data

            # Example: Redirect to a thank you page with query params
            return redirect(f"/thankyou/?name={submitted_data['first_name']}")
    else:
        form = UsersForm()

    return render(request, "userform.html", {"form": form, "submitted_data": submitted_data})

# Post Method Use
def submitform(request):
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('val1'))
            n2 = int(request.POST.get('val2'))
            finalans = n1 + n2
            data = {
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
        
        
        return HttpResponse(finalans) 
    except:
        pass
 

# def home(request):
#     return render(request, "index.html")


# def aboutUs(request):
#     return HttpResponse("Welcome to first Django app...")

# def course(request):
#     return HttpResponse("Welcome to Rishi Code")

# def courseDetails(request, courseid):
#     return HttpResponse(courseid)

