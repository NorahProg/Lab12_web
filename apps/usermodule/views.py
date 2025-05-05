# from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm

# # Create your views here.
# def registerUser(request):
#     if request.method == "POST":
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            obj = form.save()
# # should we say something here: comes next using messages
#            return redirect('login')
#     form = SignUpForm()
#     return render(request, "usermodule/register.html", {"form": form})

# def logoutUser(request):
#     logout(request)
#     return redirect('/') # to landing page 

# def loginUser(request):
#     if request.method == "POST":
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            obj = form.save()
# # should we say something here: comes next using messages
#         #    return redirect('login')
#     form = LoginForm()
#     return render(request, "usermodule/loginUser.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('login')
        else:
            messages.error(request, 'There is error.')
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'usermodule/login.html'

    def get_success_url(self):
        return reverse_lazy('list_students')


def logout_view(request):
    logout(request)  
    return redirect('login')