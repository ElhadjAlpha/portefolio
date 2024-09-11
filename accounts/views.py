from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm


# def log_in(request) :
#     template_name = 'accounts/login.html'
#     if request.POST:
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_active():
#             login(request, user)
#             redirect('posts:index')
#         else:
#             message = 'Username or password is incorrect'
    #return render(request, f'{template_name}')


def register(request) :
    template_name = 'accounts/register.html'
    form = RegisterForm
    if request.POST :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, 'Your compte is created successful')
            return redirect('accounts:login')
        else:
            messages.error(request, form.errors)
    context = {
        'message': messages,
        'form': form,
    }

    return render(request, f'{template_name}', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')



