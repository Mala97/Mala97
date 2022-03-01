from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory

# Create your views here.
from .models import*
from .forms import OrderForm

#ACCUEIL
def home(request):
     orders = Order.objects.all()          # Toutes les commandes
     customers = Customer.objects.all()    # Toutes les clients
     
     total_customers = customers.count()   # Nombres de clients
     total_orders = orders.count()         # Nombres de commandes
     delivered = orders.filter(status='Delivered').count() # Ensemble des commandes livrees
     pending = orders.filter(status='Pending').count()     # Ensenble des commandes en attende
     
     context = {'orders': orders, 'customers': customers, 'total_customers':total_customers, 'total_orders':total_orders, 'delivered':delivered,'pending':pending}     
     return render(request, 'accounts/MyPage.html', context)

#PRODUITS
def products(request):
     products = Product.objects.all()
     return render(request, 'accounts/Products.html',{'products': products})

# CLIENT
def customer(request, pk_test):   
     customer = Customer.objects.get(id=pk_test)
     orders = customer.order_set.all()
     orders_count = orders.count()
     
     context = {'customer':customer, 'orders':orders, 'orders_count':orders_count}
     return render(request, 'accounts/Customer.html', context)

# COMMANDES
def createOrder(request):
     #OrderFormSet = inlineformset_factory(Customer, Order, fields=)
     
     #customer = Customer.objects.get(id=pk) 
     
     form = OrderForm()
     
     if request.method == 'POST':
          #print('Printing Post:', request.POST)
          form = OrderForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     
     context = {'form': form}
     return render(request, 'accounts/order_form.html', context)

#MISE A JOUR DES COMMANDES
def updateOrder(request, pk_id):
     order = Order.objects.get(id=pk_id) 
     
     form = OrderForm(initial={'order': order.id})
     
     if request.method == 'POST':
          form = OrderForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
          
     context = {'form':form}
     return render(request, 'accounts/order_form.html', context)
  

def deleteOrder(request, pk_test):
     order = Order.objects.get(id=pk_test)
    
     if request.method == "POST":
          order.delete()
          return redirect('/')
          
     context = {'item': order}
     return render(request, 'accounts/delete.html', context)
  