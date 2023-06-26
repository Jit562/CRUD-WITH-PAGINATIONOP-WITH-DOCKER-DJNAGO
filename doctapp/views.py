from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator

from  .models import Product
from .forms import ProductForms

# Create your views here.

def ProductView(request):

    product = Product.objects.all().order_by('pname')
    
    context = {
        'product':product,
    }
    
    return render(request, 'home.html', context)


def ProductAdd(request):
    if request.method == "POST":
        pname = request.POST['pname']
        address = request.POST['address']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        mobile = request.POST['mobile']
        date = request.POST['date']
        message = request.POST['message']

        try:
            is_true = request.POST['is_true']
        except MultiValueDictKeyError:
            is_true = False
        
        product = Product.objects.create(pname=pname, address=address, city=city, zip_code=zip_code, mobile=mobile, date=date,message=message, is_true=is_true)

        product.save()

        return HttpResponseRedirect('/')
    else:
        return render(request, 'index.html')
    

def update_data(request,id):
    if request.method == 'POST':
        pi = Product.objects.get(id=id)
        fm = ProductForms(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = Product.objects.get(id=id)
        fm = ProductForms(instance=pi)
    return render(request,'update.html', {'form':fm})


def delete_data(request,id):
    if request.method == 'POST':
        pi = Product.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')    
