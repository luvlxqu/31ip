from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def users(request):
    if request.session.get('user_id'):
        users = User.objects.all()
        return render (request, 'users.html',{'users': users})
    else:
         return redirect('/login/')


def add_user(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/users/')
    else: 
        form = UserForm()
        return render(request, "add_user.html", {'form': form})
    
def index(request):
    if request.session.get('user_id'):
        l = request.session.get('login')
        return render(request, 'index.html', {'login': l})
    else:
        return redirect('/login/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        print('поехали')
        login = request.POST.get('login')
        password = request.POST.get('pas')

        try:
            user = User.objects.get(login = login)
        except User.DoesNotExist:
            print("пользователь не найден")
            return redirect('/login')
        
        if password != user.password:
            print("Пароль не верный")
            print(password)
            print(user.password)
            return redirect("/login")
        
        request.session['user_id'] = user.id
        request.session['login'] = user.login
        
        return redirect('/')
    
def logout_view(request):
    request.session.flush()
    return redirect('/login')
