from django.shortcuts import render
from django.http import HttpResponse

from .models import Lead

def home_page(request):
    
    leads = Lead.objects.all()
    
    # return HttpResponse('<h1>hello world</h1>')
    
    context = {
        "leads": leads
    }
    
    # return render(request, "leads/homepage.html")
    return render(request, "second_page.html", context)