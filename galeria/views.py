from django.shortcuts import render

def index(Request):
    return render(Request, 'index.html')
# Create your views here.
