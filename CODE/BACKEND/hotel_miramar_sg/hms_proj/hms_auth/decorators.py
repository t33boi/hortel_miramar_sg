from django.shortcuts import redirect
from django.urls import reverse

def unauthenticated_user(view_func):
    """
    Decorator for views that checks that the user is not authenticated.
    If the user is authenticated, they are redirected to a specified URL.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))  # Redirect to the home page or any desired URL
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func