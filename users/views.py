from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .froms import UserCreateForm, UserUpdateForm

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form":create_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                "form": create_form
            }
            return render(request, 'users/register.html', context)




class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm

        return render(request, 'users/login.html', {"login_form":login_form})

    def post(self, request):
        print(request.POST['username'], request.POST['password'])
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('books:list')
        else:
            return render(request, 'users/login.html', {"login_form": login_form})

class UserProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'users/profile.html', {"user":request.user})
        else:
            return redirect('users:login')


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully loged out.")
        return redirect('landing_page')

class UserProfileUpdate(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request,
        'users/profile_edit.html',
                      context={'form':user_update_form})

    def post(self, request):
        user_update_form = UserUpdateForm(instance=request.user,
                                          data=request.POST,
                                          files=request.FILES)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "Your informatios was successfully changed.")
            return redirect("users:profile")
        messages.error(request, "Invalid your instances.")
        return render(request, 'users/profile-edit', {'form':user_update_form})
