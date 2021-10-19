from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        'name': 'Aaron',
        'age': 18,
        'Nationality': 'Indian'

    }
    return render(request,'index.html',context)