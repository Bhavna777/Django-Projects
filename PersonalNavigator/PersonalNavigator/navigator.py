# Personal navigator 

from django.http import HttpResponse
# from django.shortcuts import render

def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)

def index(request):
    return HttpResponse('''
        <a href="https://www.djangoproject.com/">Django</a>
        <a href="https://www.youtube.com/">Youtube</a>
        <a href="https://www.google.com/">Google</a>
        <a href="https://www.freecodecamp.org/">Freecodecamp</a>
        <a href="https://www.softles.com/">Softles</a>
    ''')
