from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.shortcuts import *
from django.http import *
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
from .models import *
import re
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=rform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(username=username, password=password,
                                     email=email)
            return HttpResponseRedirect('/')
    else:
        form=rform()
    return render(request,'signup.html',{'form':form})
def login(request):
    return render(request,'login.html')
def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
     
    if user is not None:
        auth.login(request,user)

        #return HttpResponseRedirect('/')
        return HttpResponseRedirect('/updates/')
    else:
        return HttpResponse('/invalid/')
def info_f(request):
    if request.method=='POST':
        form =info_form(request.POST,request.FILES)
        print"1"
        if form.is_valid():
            obj=info(title=form.cleaned_data['title'],
                       description=form.cleaned_data['description'],
                       pos=form.cleaned_data['pos'])
            #f=obj.save()
            obj.created_by=request.user
            c=form.cleaned_data['title']
            s=['computer science','Electronics','maths','open source']
            print"2"
            for i in s:
                r=re.search(i,c,re.I)
                if r:
                    slug_name=i
            #print slug_name
            #f.slug=slug_name
            obj.save()
        return HttpResponseRedirect('/blogs/')
    
    else:
        print "hrllo"
        form=info_form()
    return render(request,'info.html',{'form':form})

def blogs(request):
    posts=info.objects.order_by('-date_created')
    #posts=info.objects.all()
    print posts
    return render(request,'blog.html',{'posts':posts})
    
def logout(request):
    auth.logout(request)
    #return render(request,'login.html')
    return HttpResponseRedirect('/')

def dashboard(request,d):
    k=User.objects.get(id=d)
    k1=info.objects.filter(created_by=k)

    return render(request,'dashboard.html',{'k':k1})


def search(request):
    if request.method=='POST':
        squery=request.POST['search_box']
        if squery:
            s=info.objects.filter(title__icontains=squery)
            print s
            if s:
                return render(request,'blog.html',{'ct':s})
            else:
              return render(request,'blog.html',{'result':'Not Found'})

    return HttpResponseRedirect('/')
def profile(request,d):
    use=User.objects.get(id=d)
    k1=info.objects.filter(created_by=use)
    print k1
    #f=info.objects.set([title])
    #print f
    return render(request,"profile.html",{'use':k1})
def Comment(request):
    if request.method =='POST':
        post_id = request.POST['feed']
        post_obj = info.objects.get(id=post_id)
        print request.POST['user_cmt']
        print "A"
        form=cmtform(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.pos=post_obj
            f.cmt_user=request.user
            f.save()

            return redirect("/blogs/")

    else:
        form = cmtform()
    return render(request,'blog.html',{'cmt':form})

def user_profile(request):
    user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            #user.profile.job_title = form.cleaned_data.get('job_title')
            user.email = form.cleaned_data.get('email')

            user.profile.location = form.cleaned_data.get('location')
            user.profile.pic = form.cleaned_data.get('pic')
            user.save()
            
            
            return HttpResponseRedirect('/blogs/')

    else:
        form = ProfileForm(instance=user, initial={
            'location': user.profile.location,
            'pic':user.profile.pic
            })
    return render(request,'profile.html',{'form':form})    
def delete(request,d):
    try:
        n=info.objects.get(id=d)
    except:
        return HttpResponse('Try Again....!')
    n.delete()
    return HttpResponseRedirect('/blogs/')