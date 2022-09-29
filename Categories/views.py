from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CategoryForm, ProductForm
from django.contrib import messages
from .models import Category, Product
# Create your views here.

@login_required(login_url="login")
def category_view(request):
    categories=None
    try:
        categories=Category.objects.all()
        for category_detail in categories:
            print(category_detail.images)
    except Exception as e:
        print(e)

    form=CategoryForm()

    if request.method=="POST":
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request,"Category Created Successfully")
            return redirect("index")

    context={"categories":categories,"form":form}

    return render(request,"index.html",context)

@login_required(login_url="login")
def update_category_details(request,pk):
    category_detail=None
    try:
        category_detail=Category.objects.filter(id=pk).first()
        
        form=CategoryForm(instance=category_detail)
        if request.method=="POST":
            form=CategoryForm(request.POST,request.FILES,instance=category_detail)
            if form.is_valid():
                form.save()
                # messages.success(request,"Category Created Successfully")
                return redirect("index")
    except Exception as e:
        print(e)

    context={"form":form}

    return render(request,"update_category.html",context)

@login_required(login_url="login")
def product_detail(request,pk):
    product_detail=None
    form=None
    try:
        product_detail=Product.objects.filter(category__id=pk)
        print(product_detail)
        form=ProductForm()
        category=Category.objects.filter(id=pk).first()
        if request.method=="POST":
            form=ProductForm(request.POST,request.FILES)
            
            if form.is_valid():
                instance=form.save(commit=False)
                instance.category=category
                instance.save()
                # messages.success(request,"Product Created Successfully")
                return redirect("product_detail")

    except Exception as e:
        print(e)

    context={"form":form,"products":product_detail,"category":category}
    return render(request,"product_details.html",context)

def delete_category(request,pk):
    category=Category.objects.filter(id=pk).first()
    category.delete()
    return redirect('index')


def delete_product(request,pk):
    product=Product.objects.filter(id=pk).first()
    product.delete()
    return redirect('index')


def Userlogout(request):
    logout(request)
    return redirect('login')