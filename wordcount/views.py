from cgitb import text
from pickle import GET
import re
from telnetlib import AUTHENTICATION
from tkinter.tix import Form
#from telnetlib import signup
from wsgiref.util import request_uri
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, 'home.html')

def adminwc(request):
    return render(request, 'adminwc.html')
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
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def usersignup(request):
    return render(request,'login.html')



def features(request):
    return render(request,'features.html')


#def refresh(request):
#    return render(request, 'home.html')



def signupaction(request):
    global fn,ln,sex,email,pwd
    if request.method=="POST":
        con=sql.connect(host="localhost",user="root",password="12345678",database='wordy')    
        cursor=con.cursor()
        data=request.POST
        for key,value in data.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                sex=value
            if key=="email":
                email=value
          
            if key=="password":
                pwd=value

        ins="insert into users values('{}','{}','{}','{}','{}','{}')".format(fn,ln,sex,email,pwd)
        cursor.execute(ins)
        con.commit()

    return render(request,'login.html')



#contact Form

def contactt(request):
    return render(request,'contact.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home/")
      
	form = ContactForm()
	return render(request, "contact.html/", {'form':form})