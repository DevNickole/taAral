from django.http import HttpResponse
from django.shortcuts import render

def LandingPage(request):
    # return HttpResponse("Hello landing page for this ta-aral")
    return render(request, 'landingpage.html')