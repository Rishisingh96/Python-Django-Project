"""
URL configuration for djangofirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangofirstproject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL (homepage)
    # path('index/', views.index, name='index'),  # Root URL (homepage)
    path('movies-us/', views.movies, name='movies'),
    path('theatres-us/', views.theatres, name='theatres'),
    path('booking-us/', views.booking, name='booking'),
    path('signup_login-us/', views.signup_login, name='signup_login'),
    path('userform/', views.userForm),
    path('submitform/', views.submitform, name='submitform'),
    path('thankyou/', views.Thankyou),
    path('calculator/', views.calculator)
    
    
    
    # path('about-us/',views.aboutUs),
    # path('course/', views.course),
    # path('course/<int:courseid>',views.courseDetails),  // only integer
    # path('course/<str:courseid>',views.courseDetails), // only String
    # path('course/<slug:courseid>',views.courseDetails), // only slug rishi-singh
    # path('course/<courseid>',views.courseDetails),  # all type of url allowed When you not know datatype 
]


# ✅ Development mode me media serve karne ke liye
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
