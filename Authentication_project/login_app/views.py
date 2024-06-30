from django.shortcuts import render,HttpResponse
from login_app import forms,models
from django.contrib.auth.models import User
# Create your views here.

def index(request):
 
  diction = {"title":"Home Page"}

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