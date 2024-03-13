from django.shortcuts import render
from datetime import datetime
from home.models import Contact, Book, Fibuy, BookSell
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    book=Book.objects.all()
    return render(request, 'index.html',{'book':book})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def sell(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        bookname=request.POST.get('bookname')
        usedyears = request.POST.get('usedyears')
        money = request.POST.get('money')
       
    
        sell = BookSell(name=name,email=email,phone=phone,bookname=bookname,usedyears=usedyears, money=money)
        
        sell.save()
    return render(request, 'sell.html')


def buy(request):
    bb = Book.objects.all()
    return render(request, 'buy.html', {'bb': bb})


def social(request):
    social = Book.objects.filter(cat='Social')
    return render(request, 'social.html', {'social': social})


def english(request):
    eng = Book.objects.filter(cat='English')
    return render(request, 'english.html', {'eng': eng})


def maths(request):
    maths = Book.objects.filter(cat='Maths')
    return render(request, 'maths.html', {'maths': maths})


def engg(request):
    en = Book.objects.filter(cat='ENGG')
    return render(request, 'engg.html', {'en': en})


def science(request):
    science = Book.objects.filter(cat='Science')
    return render(request, 'science.html', {'science': science})


def nepali(request):
    nep = Book.objects.filter(cat='Nepali')
    return render(request, 'nepali.html', {'nep': nep})


def fibuy(request, id):
    if request.method == "POST":
        id=request.POST.get('id')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        print(id)
        a=Book.objects.get(id=id)
        fibuy = Fibuy(address=address, email=email, phone=phone,prod_id=id)
        print(1)
        fibuy.save()
        a.quant=a.quant-1
        a.save()
        return render(request, 'good.html')

    if request.method == "GET":
        a = Book.objects.get(id=id)
        return render(request, 'fibuy.html', {'a': a})

def final(request):

        return render(request, 'good.html')


def good(request):
    return render(request, 'good.html')
