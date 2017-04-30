from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from mine.models import User, MyUser, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.



def welcome(request):
    return render(request,'welcome.html')





def register_data(request):
    frm = RegisterForm()
    ctx = {'form': frm}
    return render(request, 'signinpage.html', ctx)


def login_data(request):
    fm = LoginForm()
    ptx = {'fm': fm}

    return render(request, 'loginpage.html', ptx)








def loggin(request):

    if not request.method == 'POST':
        return HttpResponse('get request')

    frm = LoginForm(request.POST)

    if frm.is_valid():
        frm.cleaned_data
        uname = frm.cleaned_data['username']
        ps = frm.cleaned_data['password']
        
        u = authenticate(username=uname, password=ps)
        if u:

        # if u.is_active:
        # ....login(request, u)
        # ctx = {'user': u}

                
            return render(request, 'profile.html', {'users': uname})
        
        else:

    
            return HttpResponse('Invalid User!')
     

    else:
        return redirect('http://127.0.0.1:8000/log')



def register(request):
    if request.method == 'POST':
        frm = RegisterForm(request.POST)
        # frm.cleaned_data
    #   print (frm)
        # return HttpResponse("efgsb")
        if frm.is_valid():
            fdata = frm.cleaned_data
            uname = fdata['username']
            name = fdata['name']
            passwd = fdata['password']
            try:
                
                usr = User(username=uname)
                usr.set_password(passwd)
                usr.save()
            except:
                return HttpResponse("User already exists!")
            myusr = MyUser(user=usr, name=name,t=0)
            myusr.save()

            return render(request,"welcome.html")
        else:
            return HttpResponse("fill all the boxes")
    else:
        return HttpResponse('Nice Try!')



def him():
    pass