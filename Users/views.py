from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
       Register_form = UserRegisterForm(request.POST)
       if Register_form.is_valid():
           Register_form.save()
           username = Register_form.cleaned_data.get('username')
           messages.success(request, f'Congratulations!{username},Your account has been created! You are now able to log in')
           return redirect('Users:Login')
    else:
        Register_form = UserRegisterForm()
    return render(request, 'Users/register.html', {'Register_form': Register_form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Users/Profile.html', context)