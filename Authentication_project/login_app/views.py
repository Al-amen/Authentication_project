
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.urls import reverse
from login_app import forms,models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    diction = {}
    if request.user.is_authenticated:  
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = models.UserInfo.objects.get(user__pk = user_id)
        
        diction = {"title":"Home Page", "user_basic_info":  user_basic_info,"user_more_info":user_more_info}

    return render(request, 'login_app/index.html',context=diction)

def register(request):
    
    register = False
    
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        user_info_form = forms.UserInfoForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()       # Save the User instance directly 
            user.set_password(user.password)  # Ensure the password is hashed
            user.save() # Save the user again after setting the password
            
            user_info = user_info_form.save(commit=False) # Don't save the UserInfo instance yet
            
            user_info.user = user # Link UserInfo to the User instance that means join
            
            if 'profile_picture' in request.FILES:
                print(request.FILES['profile_picture'])
                user_info.profile_picture = request.FILES['profile_picture']
            
            user_info.save()
            
            register = True
     
    else:
        user_form = forms.UserForm()
        user_info_form = forms.UserInfoForm()
    
    diction = {"user_form":user_form, "user_info_form":user_info_form, "register":register}
    
    return render(request, 'login_app/register.html',context=diction)

def login_page(request):
    
    return render(request, 'login_app/login.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password) 
        
        if user :
            if  user.is_active:
              login(request,user)
              
              return HttpResponseRedirect(reverse('login_app:index'))
            else:
               return HttpResponse("Account is not Active")
        else :
             return HttpResponse("User credential does not match!!")
    else :
        # return render(request, 'login_app/index.html',context={})
        return HttpResponseRedirect(reverse('login_app:index'))
@login_required
def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('login_app:index'))
        
        