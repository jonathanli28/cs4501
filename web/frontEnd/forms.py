from django import forms
from django.forms import ModelForm


class UserSignupForm(ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'id': 'username'}), required=True)
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'id': 'first_name'}), required=True)
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'id': 'last_name'}), required=True)
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'input_text'}), label='Password')
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'input_text'}), label='Re-Enter Password')
'''
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data['password2']
        if password1 != password2:  # incorrectly inputted password re-enter
            raise forms.ValidationError("The passwords entered did not match.")
        return password2

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email.exists())
            raise forms.ValidationError("Email already exists.")
        return email
    '''