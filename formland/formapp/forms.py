from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'real_name', 'email', 'password1', 'password2')
from django import forms
from .models import UserProfileModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['insta', 'phonenumber']
from django import forms
from .models import MachineModel

class MachineForm(forms.ModelForm):
    class Meta:
        model = MachineModel
        fields = ['machine', 'price', 'pictures', 'description']
