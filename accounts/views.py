from django.shortcuts import render
from .forms import UserRegistrationForm


def register_user(request):
    form = UserRegistrationForm()

    context = {'form':form}
    return render(request,'accounts/register.html',context)