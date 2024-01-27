from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from . forms import MyRegFrm, LoginFrm
from . models import Product

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
    # return HttpResponse('<h1>My First Django View</h1>')

def about(request):
    if request.POST:
        n1=request.POST.get('n1')
        n2=request.POST.get('n2')
        n1=int(n1)+int(n2)
        context={'sum':n1}
        return render(request, 'myapp/about.html', context)
    else:
        return render(request, 'myapp/about.html')
    # return HttpResponse('<h1>About Page</h1>')

def signUp(request):
    if request.POST:
        form=MyRegFrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your registration is successfull')
            except Exception as e:
                messages.error(request, e)       
    else:
        form=MyRegFrm()
    return render(request, 'myapp/signUp.html', {'form':form})

def displayProduct(request):
    allprod=Product.objects.all()
    return render(request, 'myapp/dispProd.html',{'allprod':allprod})

def signin(request):
    if request.POST:
        form=LoginFrm(request=request, data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.changed_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/allprod')
    else:
        form=LoginFrm()
    return render(request, 'myapp/signIn.html', {'form':form})