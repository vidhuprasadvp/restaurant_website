from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def log(request):
    return render(request,'log.html')

def breakfast(request):
    return render(request,'breakfast.html')

def dinner(request):
    return render(request,'dinner.html')

def drinks(request):
    return render(request,'drinks.html')

def lunch(request):
    return render(request,'lunch.html')

def nightlife(request):
    return render(request,'nightlife.html')

def snacks(request):
    return render(request,'snacks.html')

def reg(request):
    return render(request,'reg.html')