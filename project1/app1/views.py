from django.shortcuts import redirect,render
from django.contrib import messages
from django.views.decorators.cache import never_cache


# Create your views here.

def login(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        use = request.POST.get('username')
        pd =  request.POST.get('pass1')
        if use =='Robin' and pd == 'asdf':
            request.session['username'] = use
            return redirect(home)
        else:
            messages.error(request,'Invalid password or username')
    return render(request,'login.html')
@never_cache
def home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    return redirect(login)

def logout(request):
    if 'username' in request.session:
        request.session.clear()
        return render(request,'login.html')
