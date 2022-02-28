
from Scripts.WebDjango.accounts.models import Customer, Order, Product
from django.db import models

# """ (1)Retourne tous les utilisateurs de la table 
customers = Customer.objects.all()

# """ (2) retourne le first customer
Firtcustomer = Customer.objects.first()

#"""(3) retourne le dernier customer
Lastcustomer = Customer.objects.last()

#"""(4) retourne un seul customer par son nom
customerByname = Customer.objects.get(name = 'Souleymane')

#"""(5) retourne un seul customer par son identifiant
customerByid = Customer.objects.get(id = 3)

#"""(6) retourne tous les particuliers du customer
Firstcustomer = Customer.order_set.all()

#"""(7) retourne tous les clients suivant les orders
order = Order.objects.first()
parentName = order.customer.name

#"""(8) retourne tous les produites venant de la table Product
products = Product.objects.filter(Category="Out Door")

#"""(9) Order/Sort objects by id 
leastToGreatest = Product.objects.all().order_by('id')
greatestToGreatest = Product.objects.all().order_by('id')

#"""(10) retourne tous les produits avec l'option Sport
productsFiltered = Product.objects.filter(tags_name='Sport')

#"""(11)
ballOrders = Firstcustomer.order_set.filter(product_name='Ball').count()

#Retourne tous le nombres de compte de products ordered
allOrders = {}

for order in Firstcustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
        
    else:
        allOrders[order.product.name] = 1
        

#Related set example
class ParentModel(models.Models):
    name = models.charField(max_length=200, null=True)
  
class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)
    
    parent = ParentModel.objects.first()
    parent.childmodel_set.all()
    
    
                      
            
    

