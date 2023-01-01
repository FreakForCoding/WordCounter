from cgitb import text
import re
from telnetlib import AUTHENTICATION
from wsgiref.util import request_uri
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

#def count(request):
#    text=request.GET['usertext']

#    word_text=text.split(' ')
    
#    word_dict={}
#    for i in word_text:
#        if i in word_dict:
#            word_dict[i]+=1
#        else:
#            word_dict[i]=1

#    return render(request, 'home.html', {'key':text, 'total':len(word_text), 'answer': word_dict, 'ans':len(text) })

#def check_space(request):
#    text=request.GET['usertext']
#    count=0
#    for i in text:
#        if  i==" ":
#          count=count+1
#          #print("Number of spaces in a string:",count)

#    return render(request, 'counter.html',{'ncount':count})


#def signupview(request):
  
#    return render(request, 'signup.html')

def login(request):
    if request.method=='GET':
            return render(request, 'login.html')

        #user=AUTHENTICATION(email=email,password=password)

        #if user is not None:
            #login(request,user)
    
 
def userLogin(request):
     if request.method=='POST':
        email=request.POST['email']
        password= request.POST['password']
        
        if email == "rohit" and password=="123":
            request.session['rohit'] = '123'
            
            return render(request, 'members.html')
        else:
            
            return render(request, 'login.html')

def userLogout(request):    
    return redirect("home")








#def refresh(request):
#    return render(request, 'home.html')

