from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .forms import *
from globals.email import EmailService


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, _('Activate you account'))
        else:
            messages.error(request, _('Invalid Credentials'))

    return render(request, 'pages/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            activation = Activation(user=user)
            activation.save()

            # send activation code
            activation_code = activation.activation_code
            activation_link = f'http://127.0.0.1:8000/user/v1/activate/{activation_code}/'
            EmailService.send_activation_email(
                activation_link,
                from_email=settings.EMAIL_HOST_USER,
                to_emails=[user.email]
            )
            messages.success(request, _(f'Account was created for {form.cleaned_data["email"]}'))
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'pages/register.html', {'form': form})


def activate_account(request, code):
    activation = Activation.objects.filter(activation_code=code).first()
    now = timezone.now()

    if not activation:
        messages.error(request, _('Invalid activation code'))
        return redirect('login')

    if (now - activation.expired_at).total_seconds() > 0:
        messages.error(request, _('Invalid / expired activation code'))
        return redirect('login')

    user = activation.user
    user.is_active = True
    user.save()

    messages.success(request, _('Account has been activated successfully'))
    return redirect('login')


def forget_password(request):
    return render(request, 'pages/forget-password.html')


@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html')


def error_404(request):
    return render(request, 'pages/404.html', status=404)


def error_401(request):
    return render(request, 'pages/401.html', status=401)


def error_500(request):
    return render(request, 'pages/500.html', status=500)
