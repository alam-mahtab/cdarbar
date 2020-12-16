from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Highlight, Schedule1,Schedule2,Schedule3, ExtendedUser, festivalurl, Inquiry
from django.contrib.auth.models import User, auth
# Create your views here.
def film_festival(request):
    high = Highlight.objects.all()
    About = "This is the about content"
    return render(request, 'film-festival.html', {'About':About,'high' : high})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('input taken')
        user = auth.authenticate(username=username, password=password)
        print('authenticated')
        if user is not None:
            auth.login(request, user)
            print('login')
            #return redirect('film_festival')
            return redirect('film-festival')
        else:
            messages.info(request, 'invalid credential')
            print('input  not taken')   
            return render(request, 'sign_in.html')    
    else:
        print('Method is get')
        return render(request, 'sign_in.html')

def signup_submission(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    dateofbirth = request.POST['dateofbirth']
    phone = request.POST['phone']
    if password == confirm_password:
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already registered")
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            #user.save();
            #print('userModel works fine')
        
            extended = ExtendedUser(dateofbirth=dateofbirth,phone=phone, CD_Id=user)
            #print('Extended Model works fine')
            extended.save()
            return render(request,'sign_in.html')
    else:
        messages.info(request,'password not matching')
        return redirect('signup')



def signup(request):
    return render(request, 'sign_up.html')
# def forgetpassword(request):
#     if request.method == 'POST':
#         return render(request, PasswordChangeView)
        
#     else:
#         print("Here")
#         return render(request, 'forget-password.html')
def schedule(request):
    schs = Schedule1.objects.all()
    schds = Schedule2.objects.all()
    schdes = Schedule3.objects.all()

    return render(request, 'schedule.html', {'schs' : schs, 'schds' : schds, 'schdes' : schdes})

def logout(request):
    auth.logout(request)
    return redirect('/')

def festiveurl(request):
    youtubelink = festivalurl.objects.latest()
    print(youtubelink)
    return render(request, {'youtubelink' : youtubelink})

def contact(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       email = request.POST['email']
       Details = request.POST['Details']
       interview = request.POST.get('interview', False)
       work_or_commision = request.POST.get('work_or_commision', False)
       other = request.POST.get('other', False)
       if request.POST.get('interview').is_selected() : 
           inquiry = Inquiry.objects.create(first_name=first_name, email=email , Details=Details,interview=True, work_or_commision=False, other=False)
           inquiry.save();
           print('INTERVIEW')
       elif work_or_commision in contact:
           inquiry = Inquiry(first_name=first_name, email=email , Details=Details,interview=False, work_or_commision=True, other=False).save()
           print('WORK-OR-COMMISION')
       elif other == True:
           inquiry = Inquiry.objects.create(first_name=first_name, email=email , Details=Details,interview=False, work_or_commision=False, other=True).save()
           print('OTHER')  
       return render(request, 'schedule.html')
    else:
        return redirect(request, 'film-festival.html', {Inquiry:'model'})
    

