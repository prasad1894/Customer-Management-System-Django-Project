from django.shortcuts import redirect, render
from .models import Customer
from .models import Products

# Create your views here.
def index(request):
    cust = Customer.objects.all()
    return render(request,'index.html',{'cust':cust})

def add(request):
    return render(request,'add.html')

def addrec(request):
    v=request.POST['vendor_id']
    s=request.POST['name']
    t=request.POST['contact_details']
    u=request.POST['address']
    w=request.POST['on_time_delivery_rate']
    x=request.POST['quality_rating_avg']
    y=request.POST['average_response_time']
    z=request.POST['fulfillment_rate']
    cust=Customer(vendor_id=v,name=s,contact_details=t,address=u,on_time_delivery_rate=w,quality_rating_avg=x,average_response_time=y,fulfillment_rate=z)
    cust.save()
    return redirect("/")

def delete(request,id):
    cust=Customer.objects.get(id=id)
    cust.delete()
    return redirect("/")

def update(request,id):
    cust=Customer.objects.get(id=id)
    return render(request,'update.html',{'cust':cust})

def uprec(request,id):
    v=request.POST['vendor_id']
    s=request.POST['name']
    t=request.POST['contact_details']
    u=request.POST['address']
    w=request.POST['on_time_delivery_rate']
    x=request.POST['quality_rating_avg']
    y=request.POST['average_response_time']
    z=request.POST['fulfillment_rate']
    cust=Customer.objects.get(id=id)
    cust.vendor_id=v
    cust.name=s
    cust.contact_details=t
    cust.address=u
    cust.on_time_delivery_rate=w
    cust.quality_rating_avg=x
    cust.average_response_time=y
    cust.fulfillment_rate=z
    cust.save()
    return redirect("/")

def products(request):
    product = products.objects.all()
    return render(request,'products.html',{'product':product})