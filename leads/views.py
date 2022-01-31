from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse('<h1>hello world</h1>')
    return render(request, "second_page.html")