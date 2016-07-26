from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Request a new user"""
    if request.method != 'POST':
        # Display blank registration
        form = UserCreationForm()

    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #log the user in and redirect to home page.
            authenticate_user = authenticate(username=new_user.username,
                                             password = request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request, 'users/register.html' ,context)
            
        
