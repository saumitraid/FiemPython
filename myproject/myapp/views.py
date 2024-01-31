from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from . forms import MyRegFrm, LoginFrm
from . models import Product, Cart
from django.http import HttpResponse


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
    if request.user.is_authenticated:
        allprod=Product.objects.all()
        return render(request, 'myapp/dispProd.html',{'allprod':allprod})
    else:
        return redirect('/signin/')

def signin(request):
    if request.POST:
        form=LoginFrm(request=request, data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/allprod/')
    else:
        form=LoginFrm()
    return render(request, 'myapp/signIn.html', {'form':form})

def signOut(request):
    logout(request)
    return redirect('/signin/')

def add_to_cart(request, p_id):
    if request.user.is_authenticated:
        product = Product.objects.get(p_id=p_id)
        cart_item, created = Cart.objects.get_or_create(product=product, 
                                                        user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('/allcart/')
    else:
        return redirect('/signin/')

def viewCart(request):
    if request.user.is_authenticated:
        cart_items=Cart.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        total_price=int(total_price)
        return render(request, 'myapp/viewCart.html', {'cart_items': cart_items, 'total_price': total_price})
    else:
        return redirect('/signin/')

def remove_cart(request,id):
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(id=id,user=request.user)
        cart_item.delete()
        return redirect('/allcart/')
    else:
        return redirect('/signin/')


