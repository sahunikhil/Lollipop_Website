from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'variable': "this is sent",
    }
    messages.success(request, "This is a test message.")
    return render(request, "index.html", context)
    

def services(request):
    #return HttpResponse("This is services page.")
    return render(request, "services.html")


def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')


    return render(request, "contactus.html")




