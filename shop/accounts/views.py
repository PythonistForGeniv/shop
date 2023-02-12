from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f'log: {username} \npass: {password}')

        user = authenticate(request, password=password, username=username)

        if user is None:

            print(f'не прошли авторизацию')

            context = {'error': 'Не правильное имя пользователя или пароль!!!'}
            return render(request, 'accounts/login.html', context)
            
        login(request, user)
    return render(request, 'accounts/login.html')