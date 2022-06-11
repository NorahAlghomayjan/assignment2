from http.client import HTTPResponse
from urllib.error import HTTPError
from django.shortcuts import render , HttpResponse
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d", gmtime()),
        "time2": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html',context)