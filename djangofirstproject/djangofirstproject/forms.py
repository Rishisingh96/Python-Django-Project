from django import forms

class UsersForm(forms.Form):
    # Text field
    first_name = forms.CharField(
        label="First Name",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )

    # Email field
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )

    # Password field
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )

    # Number field
    age = forms.IntegerField(
        label="Age",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your age'
        })
    )

    # Dropdown
    gender = forms.ChoiceField(
        label="Gender",
        choices=[('M', 'Male'), ('F', 'Female')],
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    # Checkbox
    agree_terms = forms.BooleanField(
        label="I agree to the terms & conditions",
        required=True
    )
