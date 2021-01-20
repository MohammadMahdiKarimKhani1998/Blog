from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from account.forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login, authenticate


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
        else:
            pass
        context = {'form': form}
    else:
        form = LoginForm()
        context = {'form': form}
    return render(request, 'registration/login.html', context)


class Logout(LogoutView):
    next_page = 'login'


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
    success_message = "Your profile was created successfully"

