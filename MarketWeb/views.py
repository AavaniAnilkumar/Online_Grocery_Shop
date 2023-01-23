from django.shortcuts import render,redirect
from Market.models import Category, Products,contactdb
from MarketWeb.models import Customerdetails,Cart


# Create your views here.
def home_pg(req):
    data = Category.objects.all()
    return render(req, "home.html", {'data': data})


def about_pg(req):
    data = Category.objects.all()
    return render(req, "about.html", {'data': data})


def about_d(req, dataid):
    da = Category.objects.all()
    data = Products.objects.get(id=dataid)
    return render(req, "about1.html", {'data': data, 'da': da})


def contact_pg(req):
    data = Category.objects.all()
    return render(req, "contact.html", {'data': data})


def products_pg(req):
    data = Products.objects.all()
    return render(req, "products.html", {'data': data})


def dispCateg(req, itemCateg):
    print("===itemCateg===", itemCateg)
    catg = itemCateg.upper()
    products = Products.objects.filter(Categry=itemCateg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(req, "displayCategory.html", context)


def displayProd(req, dataid):
    data = Products.objects.get(id=dataid)
    return render(req, "productDetails.html", {'data': data})

def login(request):
    return render(request,"login_or_register.html")

def loginsave(request):
    if request.method=="POST":
        u = request.POST.get('user')
        e = request.POST.get('email')
        p = request.POST.get('pass')
        c = request.POST.get('cpass')
        if p == c:
            obj = Customerdetails(username=u,email=e,password=p,confirmpassword=c)
            obj.save()
            return redirect(login)
        else:
            return render(request,'login_or_register.html',{'msg':"Sorry......password not matched "})
def customerlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("user")
        password_r = request.POST.get("pass")
        if Customerdetails.objects.filter(username = username_r,password=password_r).exists():

            request.session['user'] = username_r
            request.session['pass'] = password_r


            return redirect(home_pg)
        else:
            return render(request,'login_or_register.html',{'msg':"Sorry......password not matched "})

def logout(request):
    del request.session['user']
    del request.session['pass']
    return redirect(home_pg)

def contactsave(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('sub')
        m = request.POST.get('msg')
        obj = contactdb(name=n,email=e,subject=s,message=m)
        obj.save()
        return redirect(contact_pg)


def cart(request):
    da = Category.objects.all()
    data = Cart.objects.all()
    return render(request,"cart.html",{'da':da,'data':data})

def cartsave(request):
    if request.method=="POST":
        p = request.POST.get('productname')
        q = request.POST.get('quantity')
        t = request.POST.get('totalprice')
        obj = Cart(product=p, quantity=q, total=t)
        obj.save()
        return redirect(cart)

def itemdelete(request,dataid):
    data = Cart.objects.all()
    data.delete()
    return redirect(cart)


