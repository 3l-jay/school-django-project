"""
Django Accounts Views Documentation

These views handle user authentication functionalities such as signup, login, and logout.

Functions:
    signup_view(request):
        Renders a form for user signup. If form data is submitted, validates and creates a new user account.
        If signup is successful, logs the user in and redirects to the articles page.
        If signup is not successful, re-renders the signup form.

    login_view(request):
        Renders a form for user login. If form data is submitted, verifies the credentials and logs the user in.
        If login is successful, redirects the user to the articles page.
        If 'next' parameter is provided in the request, redirects the user to the specified next page after login.
        If login is not successful, re-renders the login form.

    logout_view(request):
        Logs out the current user and redirects to the articles page.

Dependencies:
    render: Renders HTML templates.
    redirect: Redirects to a specified URL.
    UserCreationForm: Form for user signup (imported from django.contrib.auth.forms).
    AuthenticationForm: Form for user login (imported from django.contrib.auth.forms).
    login: Logs a user in (imported from django.contrib.auth).
    logout: Logs a user out (imported from django.contrib.auth).
"""


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_view(request):
    if request.method == 'POST':
        # create & get form data from user.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # check & save valid form.
            login(request, user)
            # log the user in
            return redirect('articles:list')  # redirect to articles.
    else:  # if signup not successful.
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # verify form data.
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')  # redirect to articles.
    else:  # if login not successful.
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
