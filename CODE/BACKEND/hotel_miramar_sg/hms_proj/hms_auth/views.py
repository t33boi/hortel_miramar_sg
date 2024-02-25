from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from hms_main.models import Person
from .decorators import unauthenticated_user

# Create your views here.


# def index(request):

#     return render(request, 'welcome.html')

@unauthenticated_user
def login_view(request):
    print(request.user)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        # user = Person.objects.get(username=username)
        if user is not None:
            login(request, user)
            messages.success(request, 'User Logged in Successfully')
            print(request.user)
            print(request.user.is_authenticated)

            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password')
            pass
    return render(request, 'login.html')


@unauthenticated_user
def register(request):
    print(request.user)
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')

        if password2 == password1:
            user = Person.objects.create_user(first_name=firstname,
                                              last_name=lastname,
                                              username=username,
                                              email=email,
                                              password=password1,
                                              phoneNumber=phone,
                                              address=address)
            group = Group.objects.get(name='user')
            user.groups.add(group)
            user.save()
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('home')

        else:
            messages.error(request, 'passwords dont match')

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    print(request.user)
    return redirect('home')



