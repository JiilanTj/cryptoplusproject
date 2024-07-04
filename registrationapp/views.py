from django.shortcuts import render, redirect
from django.contrib import messages, auth
from registrationapp.models import User  # Pastikan ini mengimpor model User kustom
from profileapp.models import Profile

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        walletaddress = request.POST['walletaddress']
        phone = request.POST['phone']  # Tambahkan ini
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    walletaddress=walletaddress,
                    phone=phone,  # Tambahkan ini
                    password=password
                )
                user.save()
                
                new_profile = Profile.objects.create(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    walletaddress=walletaddress,
                    phone=phone
                )
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not match!')
            return redirect('signup')
    else:
        return render(request, 'registrationapp/register.html')

def login(request):
    return render(request, 'registrationapp/login.html')
