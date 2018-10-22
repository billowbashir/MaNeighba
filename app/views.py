from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Profile
# from .forms import NewProjectForm,NewProfileForm,RateForm


@login_required(login_url='/accounts/login/')
def home(request):
    
    return render(request,'index.html')
