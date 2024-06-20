# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('client_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
