from django.shortcuts import render
from .models import *

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def platform(request):
    return render(request, 'platform.html')

def games(request):
    games_ = Game.objects.all()
    return render(request, 'games.html', {'games': games_})

def cart(request):
    return render(request, 'cart.html')



# Create your views here.
def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        users = Buyer.objects.all()
        for user in users:
            if user.name == username:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', info)

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=username, age=age)
            info['message'] = f'Приветствуем, {username}!'

    return render(request, 'registration_page.html', info)