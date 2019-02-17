from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.shortcuts import render,redirect,HttpResponseRedirect

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm


from .models import wine

# Create your views here.


def wine_detail(request):

    wine_list= wine.objects.all()
    query = request.GET.get("q")
    if query:
        wine_list = wine_list.filter(Q(description__icontains=query)|
                                    Q(designation__icontains=query)|
                                    Q(country__icontains=query)|
                                    Q(province__icontains=query)|
                                    Q(region1__icontains=query)).distinct()
    paginator = Paginator(wine_list, 50)  # Show 50 contacts per page

    page = request.GET.get('page')
    all_wines = paginator.get_page(page)


    return render(request, 'index.html', {'all_wines': all_wines})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form' : form})

# class Detailview(generic.DetailView):
#     model = wine
#     template_name = 'detail.html'