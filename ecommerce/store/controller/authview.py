from django.shortcuts import redirect, render 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout  # Import authenticate and login
from store.forms import CustomUserForm 

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect('/login')
    context = {'form': form}
    return render(request, "store/auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")  # Corrected typo: marning to warning
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')  # Corrected typo: passsword to password
            user = authenticate(request, username=name, password=passwd)  # Corrected typo: passowrd to password
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")  # Corrected typo: Usernamed to Username
                return redirect('/login')
        return render(request, "store/auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect("/")
