from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(requset):
    form = UserCreationForm()
    return render(requset,'users/register.html',{'form':form})
