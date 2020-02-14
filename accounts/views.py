# Part 1

# from django.shortcuts import render

# def signup(request):
#     return render(request, 'signup.html')

# # Part 2

# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render

# def signup(request):
#     form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


# # # Part 3

# from django.contrib.auth import login as auth_login
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


# # Part 4: import the new form, SignUpForm

from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})