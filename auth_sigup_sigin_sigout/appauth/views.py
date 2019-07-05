from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from appauth.forms import SignUpForm


def home_view(request):
    return render(request,'home.html')


def exam_view(request):
    return render(request,"exam/exam.html")

@login_required
def python_view(request):
    return render(request,'exam/python.html')

@login_required()
def django_view(request):
    return render(request,'exam/django.html')

@login_required()
def java_view(request):
    return render(request,'exam/java.html')


def contact_view(request):
    return render(request,'contact_about/contact.html')


def about_view(request):
    return render(request,'contact_about/about.html')


def logout_view(request):
    return render(request,"contains/logout.html")

def signup_view(request):
    form=SignUpForm()
    if request.method=="POST":
        # if form.is_valid():
        #     form.save()
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'contains/signup.html',{'form':form})