from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp/home.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp/home.html')  # Перенаправление на вашу главную страницу после успешного входа
        else:
            # Обработка ошибки аутентификации (например, вывод сообщения об ошибке)
            pass
    return render(request, 'myapp/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('myapp/home.html')

def home(request):
    return render(request, 'myapp/home.html')

def feedback(request):
    return render(request, 'myapp/feedback.html')

