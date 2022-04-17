from time import time
from django.shortcuts import render, HttpResponse
from matplotlib.style import context
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # context = {
    #     'variable1':"Swaraj is great",
    #     'variable2':"Rohan is great"
    # }
    return render(request, 'index.html')
    # return HttpResponse("this is a home page")

def about(request):
        return render(request, 'about.html')

    # return HttpResponse("this is a about page")

def services(request):
        return render(request, 'services.html')

    # return HttpResponse("this is a services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phon = request.POST.get('phon')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phon=phon, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

    # return HttpResponse("this is a contact page")