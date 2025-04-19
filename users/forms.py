from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'bg-[#008CFF59] py-4 px-8 rounded-full w-full form-control',
            'placeholder': 'Phone number:'
        })
    )

    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'bg-[#008CFF59] py-4 px-8 rounded-full w-full form-control',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'role']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'bg-[#008CFF59] py-4 px-8 rounded-full w-full form-control',
                'placeholder': 'Username:',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'bg-[#008CFF59] py-4 px-8 rounded-full w-full form-control',
                'placeholder': 'Email:',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'bg-[#008CFF59] py-4 px-8 rounded-full w-full form-control',
                'placeholder': 'Password:',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'bg-[#008CFF59] py-4 px-8 rounded-full w-full form-control',
                'placeholder': 'Confirm Password:',
            }),
        }
