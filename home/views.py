from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    areas = Center.objects.values_list('area', flat=True)
    if request.user.is_authenticated:
        books = Booking.objects.filter(user=request.user)
        totbooks = len(books)
    else:
        totbooks = 0
        books = None
    context = {
        'areas':areas,
        'books':books,
        'totbooks': totbooks,
    }
    return render(request, 'index.html', context)

def signout(request):
    logout(request)
    return redirect(index)

def signup(request):
    return render(request, 'pre-reg.html')

def signin(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        passwd = request.POST.get("passwd")
        user = authenticate(username = uname, password = passwd)

        if user is not None:
            login(request,user)
            return redirect(index)
            
        else:
            messages.error(request, "Wrong Credentials!")
            return HttpResponseRedirect(request.path_info)
    return render(request, 'login.html')


def individual_signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        uname = request.POST.get("uname")
        phone = request.POST.get("phone")
        passwd1 = request.POST.get("passwd1")
        passwd2 = request.POST.get("passwd2")
        user = User.objects.filter(username = uname)

        if user.exists():
            messages.error(request, "User already exists! Choose a different username", extra_tags="signup")
            return HttpResponseRedirect(request.path_info)
        else:
            if passwd1 != passwd2:
                messages.warning(request, "Retyped Password did not match. Please try again", extra_tags="signup")
                return HttpResponseRedirect(request.path_info)
            else:
                user = User.objects.create(username = uname, email=email)
                user.set_password(passwd1)
                iusr = IUser()
                iusr.user = user
                iusr.phone = phone
                iusr.save()
                user.save()
                user = authenticate(username = uname, password = passwd1)
                login(request,user)
                return redirect(index)
    return render(request, 'i_reg.html')

def center_signup(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        oname = request.POST.get("oname")
        photo = request.FILES['photo']
        passwd1 = request.POST.get("passwd1")
        passwd2 = request.POST.get("passwd2")
        area = request.POST.get("area")
        phone = request.POST.get("phone")
        halltype = request.POST.get("halltype")
        user = User.objects.filter(username=uname)

        if user.exists():
            messages.error(request, "Email/Username already exists! Choose a different one")
            return HttpResponseRedirect(request.path_info)
        else:
            if passwd1 != passwd2:
                messages.warning(request, "Retyped Password did not match. Please try again")
                return HttpResponseRedirect(request.path_info)
            else:
                user = User.objects.create(username=uname)
                user.set_password(passwd1)
                center = Center()
                center.user = user
                center.email = email
                center.phone = phone
                center.area = area
                center.picture = photo
                center.cname = oname
                center.halltype = halltype
                center.save()
                user.save()
                user = authenticate(username = uname, password = passwd1)
                login(request,user)
                return redirect(addMore)
    return render(request, 'o_reg.html')



class searchPage(View):

    def get(self, request, *args, **kwargs):
        areas = Center.objects.values_list('area', flat=True)
        area = self.request.GET.get('area')
        halltype = self.request.GET.get('halltype')
        centers = Center.objects.filter(area=area , halltype=halltype)
        # print(centers)
        tot = len(centers)
        
        context ={
            'centers':centers,
            'tot':tot,
            'areas':areas,
            'area':area,
            'halltype':halltype,
        }

        return render(request, 'search.html', context)


def getCenter(request, slug):
    center = Center.objects.get(slug=slug)
    context = {
        'center': center
    }
    return render(request, 'com-page.html', context)

@login_required(login_url='/login')
def bookCenter(request, slug):
    center = Center.objects.get(slug=slug)
    if request.method == "POST":
        eventType = request.POST.get("eventType")
        date = request.POST.get("date")
        trxid = request.POST.get("trxid")
        book = Booking()
        book.center = center
        book.date = date
        book.user = request.user
        book.eventType = eventType
        book.trxid = trxid
        book.cost = center.rent
        book.save()
        return redirect(confirmBooking)
        
    context = {
        'center': center
    }
    return render(request, 'book.html', context)


def confirmBooking(request):
    return render(request, 'confirmbook.html')

def addMore(request):

    center = Center.objects.get(user=request.user)
    if request.method == "POST":
        rent = request.POST.get("rent")
        capacity = request.POST.get("capacity")
        fullAdd = request.POST.get("fullAdd")
        isAvailable = request.POST.get("isAvailable")
        fbLink = request.POST.get("fbLink")
        igLink = request.POST.get("igLink")
        if isAvailable == "True":
            isAvailable = True
        else:
            isAvailable = False
        center.rent = rent
        center.capacity = capacity
        center.fullAdd = fullAdd
        center.isAvailable = isAvailable
        center.fbLink = fbLink
        center.igLink = igLink
        center.save()
        return redirect(addMore)
    return render(request, 'addMore.html')