from django.shortcuts import render, redirect
from user.models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as log_out


# Handles user signup functionality
# If the request method is POST, it processes the form data to create a new user
# If passwords match, the user is created and logged in; otherwise, an error message is shown
def signup(request):
    message = None
    error_message = None
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = Profile.objects.create_user(
                email,
                email,
                password1
            )
            user.first_name = fname
            user.last_name = lname
            user.save()
            login(request,user)
            return redirect('Home')
        else:
            error_message = "Passwords not match"

    return render(request, 'signup.html', {'message':message,'error_message':error_message})

# Handles user signin functionality
# Authenticates the user with the provided email and password
# If successful, logs the user in and redirects to the home page; otherwise, shows an error
def signin(request):
    error_message = None
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            error_message = "Email or Password is incorrect"

    return render(request, 'signin.html', {'error_message':error_message})

# Renders the receipt page
def receipt(request):
    return render(request, 'receipt.html')

# Renders the my account page for the user
def my_account(request):
    return render(request, 'my_account.html')

# Logs out the user and redirects to the home page
def logout(request):
    log_out(request)
    return redirect('Home')