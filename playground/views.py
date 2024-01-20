from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request-> response
# Request Handler 
#action
def say_hello(request): 
     #Pull data from db
    # Transform data
    #send Email 
    
    # return HttpResponse('Hello World')
    # return http template 
    
    return render(request,"hello.html",{'name':'Parth'})
   
    


    
    