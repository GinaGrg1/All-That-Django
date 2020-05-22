from django.shortcuts import render
from django.http import HttpResponse

import random
import string
import re

def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    length = int(request.GET.get('length'))  # Gets the length variable from home.html
 
    if request.GET.get('uppercase'):
        thepassword = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    if request.GET.get('special'):      
        while True:
            thepassword = ''.join(random.choice(string.ascii_letters + '[@_!#$%^&*()<>?/\|}{~:]') for _ in range(length))
            if regex.search(thepassword):
                break
    if request.GET.get('numbers'):
        while True:
            thepassword = ''.join(random.choice(string.ascii_letters + '[@_!#$%^&*()<>?/\|}{~:]' + string.digits) for _ in range(length))
            if regex.search(thepassword) and any(p.isdigit() for p in thepassword):
                break

    return render(request, 'generator/password.html', {'password': thepassword})
