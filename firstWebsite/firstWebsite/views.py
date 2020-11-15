# I have created this file :- Bhavna

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''
        <h1><a href="/">Home</a></h1>
        <h1><a href="/about">About</a></h1>
        <h1><a href="/blog">Blog</a></h1>
        <h1><a href="/contact">Contact</a></h1>
        <h1><a href="/project">Project</a></h1>

    ''')
    # return render(request, 'index.html')

def about(request):
    return HttpResponse('''
        <h1>About</h1>
        <input type=button value="Back" onClick="javascript:history.go(-1);">
    ''')

def blog(request):
    return HttpResponse('''
        <h1>Blog</h1>
        <input type=button value="Back" onClick="javascript:history.go(-1);">
    ''')

def contact(request):
    return HttpResponse('''
        <h1>Contact</h1>
        <input type=button value="Back" onClick="javascript:history.go(-1);">
    ''')

def project(request):
    return HttpResponse('''
        <h1>Project</h1>
        <input type=button value="Back" onClick="javascript:history.go(-1);">
    ''')