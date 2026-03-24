from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    """
    View for the about page.
    """
    context = {
        'title': 'About Us',
        'description': 'Learn more about our application.'
    }
    return render(request, 'about.html', context)