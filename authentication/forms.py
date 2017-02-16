from django import forms

from .models import TestUser


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=128)
    password = forms.CharField(min_length=5, max_length=128)
    password_repeat = forms.CharField(min_length=5, max_length=128)
    email = forms.EmailField()

    class Meta:
        model = TestUser
        exclude = ['user']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            user = TestUser.objects.get(user__username=username)
            raise forms.ValidationError('This username already exsit!')
        except TestUser.DoesNotExist:
                return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            email = TestUser.objects.get(user__email=email)
            raise forms.ValidationError('This email already used!')
        except TestUser.DoesNotExist:
            return email

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError('Passwords does not match!')
        return password_repeat

    def save(self):
        user = super(RegistrationForm, self).save()
        return user
