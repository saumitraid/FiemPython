import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from . forms import MyRegFrm, LoginFrm
from . models import Product, Cart, Order
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
    allprod=Product.objects.all()
    return render(request, 'myapp/dispProd.html',{'allprod':allprod})

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

def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST["amount"]) * 100  # Amount in paise
        address=request.POST['address']
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data = {
            "amount": amount,
            "currency": "INR",
            "receipt": "order_receipt",
            "notes": {
                "email": "user_email@example.com",
            },
        }

        order = client.order.create(data=payment_data)
        
        # Include key, name, description, and image in the JSON response
        response_data = {
            "id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": settings.RAZORPAY_API_KEY,
            "name": "My Project",
            "description": "Payment for Your Product",
            "image": "https://yourwebsite.com/logo.png",  # Replace with your logo URL
        }
        cart_items=Cart.objects.filter(user=request.user)
        # payment_id=response_data.id
        for cart in cart_items:
            Order.objects.get_or_create(user=request.user, product= cart.product, quantity=cart.quantity, payment_status='success', address=address)
        
        Cart.objects.filter(user=request.user).delete()

        return JsonResponse(response_data)
    return redirect('myapp:viewCart.html')

def payment_success(request):
    return render(request, "cart/payment_success.html")

def payment_failed(request):
    return render(request, "cart/payment_failed.html")


