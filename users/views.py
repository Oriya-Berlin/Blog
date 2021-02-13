from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterForm


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('blog-home-page')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

