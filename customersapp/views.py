from django.shortcuts import render,redirect
from .models import Customers,CustomersForm       
  
def add_customers(request):
    if request.method=="POST":
        form=CustomersForm(request.POST)
        context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,"addcustomers.html",context)
    else:
        form=CustomersForm
        context={'form':form}
        return render(request,"addcustomers.html",context)
    

def customers_list(request):
    clist=Customers.objects.all()
    context={'clist':clist}
    return render(request,'customerslist.html',context)


def delete_customers(request,id):
    clist = Customers.objects.get(id=id)
    clist.delete()
    return redirect('/')

def edit_customers(request,id):
    clist = Customers.objects.get(id=id)
    if request.method == 'POST':
        clist = CustomersForm(request.POST,instance=clist)
        clist.save()
        return redirect('/')
    else:
        clist = CustomersForm(instance =clist)
        context = {'form':clist}
        return render(request,'addcustomers.html',context)




