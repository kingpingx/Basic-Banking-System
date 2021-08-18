from django.shortcuts import redirect, render, HttpResponse
from app1.models import Customer, Transaction
from django.contrib import messages
from django.contrib.auth import authenticate
from django.db.models import F
from datetime import datetime


# Create your views here.
def login(request):
    if request.method== 'POST':
        loginid = request.POST.get('username')
        pass_word= request.POST.get('password')
        print(loginid, pass_word)
        x=authenticate(username=loginid, password=pass_word)
        if x is None:
            return render(request, 'login.html',{'mess' : 'Invalid Credentials'})
        else:
            return redirect('homepage/')
            
    else:
        return render(request, 'login.html')

def homepage(request):
    return render(request,'homepage.html') 

def view_customer(request):
    customer = Customer.objects.all()
    if request.method == 'POST':
        if request.POST.get('name'):
            name = request.POST.get('name')
            cust = Customer.objects.get(name=name)
            return render(request,'view_customer.html',{'cv':cust, 'vc': customer})
        else:
            return render(request,'view_customer.html',{'vc':customer})
    else:
        return render(request,'view_customer.html',{'vc':customer}) 

    
def transfer(request):
    customer = Customer.objects.all()
    if request.method == 'POST':
        sender = request.POST.get('sname')
        reciever = request.POST.get('rname')
        scust = Customer.objects.get(name=sender)
        money = float(request.POST.get('amount'))
        if sender!=reciever and scust.amount>=money:
            if money>0: 
                scust.amount = (scust.amount-money)
                scust.save()
                rcust = Customer.objects.get(name=reciever)
                rcust.amount = (rcust.amount+money)
                rcust.save()    
                transfer = Transaction(sname=sender,rname=reciever,money=money,tdate=datetime.today())
                transfer.save()
                return render(request, 'transfer.html',{'vc':customer})
            else:
                return render(request, 'transfer.html',{'vc':customer})
        else:
            return render(request,'transfer.html',{'vc':customer})

    else:
        return render(request,'transfer.html',{'vc':customer})
    
def transactions(request):
    transaction = Transaction.objects.all()
    return render(request,'transactions.html',{'tc':transaction})