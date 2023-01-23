from django.contrib.auth import authenticate, login
from django.contrib.auth.models import  User
from django.shortcuts import render, redirect
from Market.models import Admins, Category, Products
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home(req):
    return render(req, "index.html")


def add_admin(req):
    return render(req, "Add_admin.html")


def save_admin(req):
    if req.method == "POST":
        na = req.POST.get('name')
        mob = req.POST.get('mob')
        em = req.POST.get('email')
        us = req.POST.get('user')
        pw = req.POST.get('pwd')
        cp = req.POST.get('con')
        im = req.FILES['img']
        obj = Admins(Name=na, Mobile=mob, Email=em, Username=us, Password=pw, Confirm=cp, Image=im)
        obj.save()
        return redirect(add_admin)


def view_admin(req):
    return render(req, "View_admin.html")


def display_ad(req):
    data = Admins.objects.all()
    return render(req, "View_admin.html", {'data': data})


def edt_adm(req, dataid):
    data = Admins.objects.get(id=dataid)
    print(data)
    return render(req, "Edit_adm.html", {'data': data})


def upd_adm(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        mob = req.POST.get('mob')
        em = req.POST.get('email')
        us = req.POST.get('user')
        pw = req.POST.get('pwd')
        cp = req.POST.get('con')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Admins.objects.get(id=dataid).Image
        Admins.objects.filter(id=dataid).update(Name=na, Mobile=mob, Email=em, Username=us, Password=pw, Confirm=cp, Image=file)
        return redirect(display_ad)


def del_adm(req, dataid):
    data = Admins.objects.filter(id=dataid)
    data.delete()
    return redirect(display_ad)


def add_categ(req):
    return render(req, "Add_categ.html")


def save_categ(req):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('desc')
        im = req.FILES['img']
        obj = Category(Name=na, Description=de, Image=im)
        obj.save()
        return redirect(add_categ)


def view_categ(req):
    return render(req, "View_categ.html")


def display_categ(req):
    data = Category.objects.all()
    return render(req, "View_categ.html", {'data': data})


def edit_categ(req, dataid):
    data = Category.objects.get(id=dataid)
    print(data)
    return render(req, "Edit_categ.html", {'data': data})


def update_categ(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('desc')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=dataid).Image
        Category.objects.filter(id=dataid).update(Name=na, Description=de, Image=file)
        return redirect(display_categ)


def delete_categ(req, dataid):
    data = Category.objects.filter(id=dataid)
    data.delete()
    return redirect(display_categ)


def add_prod(req):
    data = Category.objects.all()
    return render(req, "Add_product.html", {'data': data})


def save_prod(req):
    if req.method == "POST":
        na = req.POST.get('name')
        pr = req.POST.get('price')
        qu = req.POST.get('quant')
        de = req.POST.get('desc')
        im = req.FILES['img']
        cat = req.POST.get('categ')
        obj = Products(Name=na, Price=pr, Quantity=qu, Description=de, Image=im, Categry=cat)
        obj.save()
        return redirect(add_prod)


def view_prod(req):
    return render(req, "View_product.html")


def display_prod(req):
    data = Products.objects.all()
    return render(req, "View_product.html", {'data': data})


def edit_prod(req, dataid):
    data = Products.objects.get(id=dataid)
    da = Category.objects.all()
    return render(req, "Edit_product.html", {'data': data, 'da': da})


def update_prod(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        pr = req.POST.get('price')
        qu = req.POST.get('quant')
        de = req.POST.get('desc')
        cat = req.POST.get('categ')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Products.objects.get(id=dataid).Image
        Products.objects.filter(id=dataid).update(Name=na, Price=pr, Quantity=qu, Description=de, Image=file, Categry=cat)
        return redirect(display_prod)


def delete_prod(req, dataid):
    data = Products.objects.filter(id=dataid)
    data.delete()
    return redirect(display_prod)


def show(req):
    return render(req, "test.html")


def log(req):
    return render(req, "login.html")


def adminlog(req):
    if req.method == "POST":
        user_r = req.POST.get('user')
        pwd_r = req.POST.get('pwd')

        if User.objects.filter(username__contains=user_r).exists():
            us = authenticate(username=user_r, password=pwd_r)

            if us is not None:
                login(req, us)
                req.session['username'] = user_r
                req.session['password'] = pwd_r
                return redirect(home)

            else:
                return redirect(log)

        else:
            return redirect(log)


# def adminlogin(request):
#     if request.method=="POST":
#         username_r = request.POST.get('user')
#         password_r = request.POST.get('pwd')
#
#         if User.objects.filter(username__contains=username_r).exists():
#             user = authenticate(username=username_r, password=password_r)
#             if user is not None:
#                 login(request, user)
#                 request.session['username']=username_r
#                 request.session['password']=password_r
#                 return redirect(home)
#             else:
#                 return redirect(log)
#         else:
#             return redirect(log)
