from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Order, Product, Customer
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter



def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    return render(request, 'accounts/register.html', {
        'form': CreateUserForm()
    })

def loginView(request):
    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return redirect('/login')
    return render(request, 'accounts/login.html', {
        # 'form': form
    })

def logoutView(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {
        'products': products
    })


@login_required(login_url='/login')
def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()

    return render(request, 'accounts/dashbaord.html', {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'pending': pending
    })

@login_required(login_url='/login')
def customer(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        total_orders = Order.objects.filter(customer=customer).count()
        orders = Order.objects.filter(customer=customer)
        filter = OrderFilter(request.GET, queryset=orders)
        orders = filter.qs
    except Customer.DoesNotExist:
        customer = None
    return render(request, 'accounts/customer.html', {
        'customer': customer,
        'total_orders': total_orders,
        'orders': orders,
        'filter': filter
    })

@login_required(login_url='/login')
def create_order(request, pk):

    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={
        'customer': customer
    })



    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')


    return render(request, 'accounts/order_form.html', {
        'form': form,
        'customer': customer
    })

@login_required(login_url='/login')
def update_order(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    return render(request, 'accounts/order_form.html', {
        'form': OrderForm(instance=order),
        'order': order
    })


@login_required(login_url='/login')
def remove_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('/dashboard')