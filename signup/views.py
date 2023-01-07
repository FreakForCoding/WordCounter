
from multiprocessing import Value
from django.shortcuts import render
import mysql.connector as sql

fn=''
ln=''
sex=''
email=''
pwd=''

# Create your views here.
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

        ins="insert into auth_user Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,sex,email,pwd)
        cursor.execute(ins)
        con.commit()

    return render(request,'signup.html')