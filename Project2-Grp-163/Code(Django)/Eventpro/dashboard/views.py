
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views import generic
from .models import Event, Booking
from . forms import *


def event_list(request):
    events = Event.objects.all()
    return render(request, 'dashboard/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'dashboard/event_detail.html', {'event': event})

def book_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']
        number_of_tickets = request.POST['number_of_tickets']
        booking = Booking.objects.create(
            event=event,
            customer_name=customer_name,
            customer_email=customer_email,
            number_of_tickets=number_of_tickets
        )
        return redirect('event_list')
    return render(request, 'dashboard/book_event.html', {'event': event})

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'dashboard/index.html', {'form': form})
    # return render(request,'dashboard/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = auth.authenticate(username=username,password=password1)
        if user is not None:
             auth.login(request, user)
             return redirect('/')
        else:
             messages.info(request,'inavlid credentials')
             return redirect('login')
    else: 
        return render(request,'dashboard/login.html') 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        if (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() ):
                messages.error(request, 'Username or email exists already')
                return redirect('register')
        if password1 == password2:
            user = User.objects.create_user(username=username,password=password1,email=email)
            user.save()
            messages.success(request, 'You have successfully registered')
            return redirect('login')
        else:
        # Save the user to the database
        # ...
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'dashboard/register.html')

def clubpage(request):
    return render(request,"dashboard/club.html")
def eventpage(request):
    return render(request,"dashboard/Events_hai.html")
@login_required
def clubdash(request):
    return render(request,"dashboard/clubdash.html")
def gallerypage(request):
    return render(request,"dashboard/G.html")

@login_required
def Dash(request):
    return render(request,"dashboard/Dash.html")

@login_required
def eventdash(request):
    events = Event.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = Event.objects.get(name=form.cleaned_data['eventname'])
            booking.save()
            return redirect('payment')
    else:
        form = BookForm()
    context = {'form':form,'events': events}
    return render(request,"dashboard/eventdash.html",context)
# def eventdash(request):
#     events = Event.objects.all()
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('payment')
#     else:
#         form = BookForm()
#     context = {'form':form,'events': events}
#     return render(request, 'dashboard/eventdash.html', context)

@login_required
def messagedash(request):
    
    return render(request,"dashboard/messagedash.html",)




def forgotp(request):
    return render(request,"dashboard/Forpvid.html")
def usercal(request):
    return render(request,"dashboard/user_cal.html")


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return HttpResponse("Payment Successful")
    else:
        form = PaymentForm(request=request)
        # return redirect('home')
        return HttpResponse("Payment UnSuccessful")

    return render(request, 'dashboard/payment.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')


# def contact(request):
#     return HttpResponse("wokring")