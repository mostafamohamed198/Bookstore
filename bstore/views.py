from turtle import position
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

@csrf_exempt
@login_required
def addcomments(request):
    if request.method == 'POST':
        print('posted')
        data= json.loads(request.body)

        comment = data.get('thecomment')
        commentuser = data.get('thecommentuser')
        commentbook = data.get('thecommentbook')
            
        # cuser = User.objects.get(id = commentuser)
        cbook = books.objects.get(id = commentbook)

        thecommentt = comments(
            comment=comment,
            commentuser=request.user, 
            commentbook=cbook
        )
        thecommentt.save()
    return JsonResponse({"message": "Email sent successfully."}, status=201)

    
def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")



def newbook(request):
    # allcategories = categories.objects.all()
    form = BookForm()
    rward = RewardForm()
    if request.method == 'POST':
        print('post')
        form = BookForm(request.POST, request.FILES)
        therewards = RewardForm(request.POST, request.FILES)
        for rewaaard in therewards:
            print(rewaaard)
        print(therewards)
        therewardname = request.POST['rewardname']
        print(therewardname)
       
        if form.is_valid():
            print('valid')
            
            therewards.save()
            # print(therewards)
            therewward = rewards.objects.get(rewardname = therewardname)
            print(therewward)
            t = form.save(commit=False)
            t.bookuser = request.user
            t.save()
            
            t.bookrewards.add(therewward) 
        else:
            print('invalid')
            print(form.errors)
    
    return render(request, "network/newbook.html", {'form': form, 'reward':rward})

def book(request, id):
    submitedbook = books.objects.get(id=id)
    bkchapters = chapters.objects.filter(chapterbook=submitedbook)
    submitedbookrewards = submitedbook.bookrewards.all()

    bookcomments = comments.objects.filter(commentbook= submitedbook)
    return render(request, 'network/book.html', {'book':submitedbook, 'chapters':bkchapters,  'comments':bookcomments, 'rewards':submitedbookrewards})

def chapterssubmit(request, idd):
    if request.method == 'POST':
        print('ok')
        chapternum = request.POST['chapternumber']
        chapterdes = request.POST['chapterdescription']
        thebook = books.objects.get(id= idd)
        chapters.objects.create(chapterbook = thebook, chapternumber= chapternum, chapterdescription = chapterdes )
    return render(request, 'network/submitchapter.html')

def rewardssubmit(request, iddd):
    rward = RewardForm()
    if request.method == 'POST':
        print('post')
        form = RewardForm(request.POST, request.FILES)
        therewardname = request.POST.getlist('rewardname')
        for reward in therewardname:
            print(reward)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
        else:
            print(form.errors)
    
    return render(request, 'network/submitreward.html', {'reward':rward})

@csrf_exempt
def testing(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first = data.get('first')
        second = data.get('second')

        testt = test(
            first=first,
            second=second
        )

        testt.save()
        return JsonResponse({"message": "Email sent successfully."}, status=201)
    
def testt(request):
    return render(request, 'network/test.html')

def cards(request):
    categorries =categories.objects.all()
    bookks = books.objects.all()
    return render(request, 'network/cards.html', {'categories':categorries, 'books':bookks})

def allcategories(request, idddd):
    allcategories = categories.objects.get(id=idddd)
    categorybook =books.objects.filter(bookcategory=allcategories)
    return render(request, 'network/categories.html', {'categorybook':categorybook, 'category':allcategories})


@csrf_exempt
def cart(request, book_id):
    cart_book = books.objects.get(id=book_id)
    if request.method =='PUT':
        print('we\'ve hit put')

        data = json.loads(request.body)

        if data.get('cart') is not None:
            print('in cart')
            cart_book.addtocart.add(request.user)

        elif data.get('notcart') is not None:
            print('not in like')
            cart_book.addtocart.remove(request.user)

        print('about to render')


def thecart(request):
    userr = request.user
    usercart = books.objects.filter(addtocart = userr)
    if request.method == 'POST':
        address = request.POST['address']
        phone = request.POST['phone']
        reqbooks = request.POST['reqbooks']
        print(reqbooks, address)
        therequest = requests.objects.create(requesteduser = request.user, requestaddress= address, requestphone = phone)
        therequest.save()
        # while i < len(reqbooks):
        #     print(int(reqbooks))
        #     therequest.requestedbooks.add(reqbooks[i])
        #     i = i+25
        #     print('finished')
        #     print(i)

        for book in usercart:
            print(book.id)
            therequest.requestedbooks.add(book)
    return render(request,'network/cart.html', {'usercart' :usercart})

def therequests(request):
    thereq = requests.objects.filter(finished = False)
    return render(request, 'network/request.html', {'requests': thereq})

@csrf_exempt
def finished(request, iddddd):
    if request.method == 'PUT':
        print('put')
        data = json.loads(request.body)

        if data.get('finished') is not None:
            print('in cart')
            therequ = requests.objects.get(id=iddddd)
            print(therequ.finished)
            therequ.finished = True
            print(therequ.finished)
            therequ.save()
    return JsonResponse({"message": "Email sent successfully."}, status=201)

def requestdetails(request, idddddd):
    detail = requests.objects.get(id=idddddd)
    return render(request, 'network/requestdetails.html',{'detail':detail})
