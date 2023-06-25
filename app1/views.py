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
            print("Invalid Credentials"	)
            return render(request, 'login.html',{'mess' : 'Invalid Credentials'})
        else:
            print("Login Successful")
            return redirect('homepage/')
            
    else:
        return render(request, 'login.html')

def homepage(request):
    return render(request,'homepage.html') 

def view_customer(request):
    customer = Customer.objects.all()
    #get customer field so we can add a customer from html form
    if customer is None or len(customer)==0:
        print("in if")
        messages.error(request, "No customers found")
        return render(request,'add_customer.html')
    else:
        print("in else")
        print(customer)
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
    if customer is None:
        messages.error(request, "No customers found")
        return render(request,'transfer.html')
    else:
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
    if transaction is None:
        messages.error(request, "No transactions found")
        return render(request,'transactions.html')
    else:
        return render(request,'transactions.html',{'tc':transaction})

def add_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        type = request.POST['type']
        phone = request.POST['phone']
        amount = request.POST['amount']

        customer = Customer.objects.create(
            name=name,
            email=email,
            type=type,
            phone=phone,
            customer_id=Customer.objects.count()+1,
            transaction_date=datetime.today(),
            amount=amount
        )

        # Redirect to the customer list page
        return redirect('customer')
    else:    
        return render(request, 'add_customer.html')