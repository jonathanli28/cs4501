from django import forms


class LogForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class UserSignupForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs = {'id': 'username'}), required=True)
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'id': 'first_name'}), required=True)
    last_name = forms.CharField(widget = forms.TextInput(attrs = {'id': 'last_name'}), required=True)
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'input_text'}), label='Password')
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'input_text'}), label='Re-Enter Password')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data['password2']
        if not password2:
            raise forms.ValidationError("Please confirm password.")
        if password1 != password2:  # incorrectly inputted password re-enter
            raise forms.ValidationError("The passwords entered did not match.")
        return password2

class CreateListingForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs = {'id': 'name'}))
    bike_style = forms.CharField(widget = forms.TextInput(attrs = {'id': 'bike_style'}))
    brake_style = forms.CharField(widget = forms.TextInput(attrs = {'id': 'brake_style'}))
    color = forms.CharField(widget = forms.TextInput(attrs = {'id': 'color'}))
    frame_material = forms.CharField(widget = forms.TextInput(attrs = {'id': 'frame_material'}))
    speeds = forms.CharField(widget = forms.TextInput(attrs = {'id': 'speeds'}))
    package_height = forms.CharField(widget = forms.TextInput(attrs = {'id': 'package_height'}))
    shipping_weight = forms.CharField(widget = forms.TextInput(attrs = {'id': 'shipping_weight'}))
    wheel_size = forms.CharField(widget = forms.TextInput(attrs = {'id': 'wheel_size'}))
    bike_description = forms.CharField(widget = forms.TextInput(attrs = {'id': 'bike_description'}))