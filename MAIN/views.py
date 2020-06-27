from django.shortcuts import render
from .models import User

from .forms import *
# Create your views here.
def register_form(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_user = User.objects.create_user(email=email, password=password)
            new_user.save()
    else:
        form = RegisterForm()
    
    context = {
        'form':form,
    }

    return render(request, 'register.html', context)