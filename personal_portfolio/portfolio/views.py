from django.shortcuts import render
from .models import Project

def home(request):
    all_fields = Project.objects.all()  # Grabs all the rows from the table
    # passing in the dictionary allows the db objects to be viewed on the homepage
    return render(request, 'pages/home.html', {'projects':all_fields})
