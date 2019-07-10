from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form':form})



# Create your views here.
