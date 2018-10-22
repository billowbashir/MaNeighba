from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Profile,Business
from .forms import NewNeighbourhoodForm
from django.views import generic


@login_required(login_url='/accounts/login/')
def home(request):
   neighbourhood=Neighbourhood.objects.all()
   return render(request,'index.html',{"neighbourhood":neighbourhood,})

@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = current_user
            neighbourhood.save()
        return redirect('Home')

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})
# class neighbourhood_details(generic.DetailView):
#     model=Neighbourhood
#     template_name='details.html'
def  neighbourhood_details(request,neighbourhood_id):
    neighbourhood=Neighbourhood.objects.get(pk=neighbourhood_id)
    return render(request,'details.html',{'neighbourhood':neighbourhood,})
