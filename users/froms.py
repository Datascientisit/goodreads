from django import forms
from django.core.mail import send_mail

from users.models import CustomUser

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", 'first_name', 'last_name', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        #send email
        # if user.email:
        #     x = send_mail(
        #         "Wellcome to Goodreads Clone",
        #         f"Hi, {user.username.title()} Welcome to Goodreads clone. Enjoy the books and reviews",
        #         "ahrorbey.ds0111@gmail.com",
        #         [user.email]
        #     )
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields = ("username", 'first_name', 'last_name', 'email', 'profile_picture')
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class':'form-control'})


