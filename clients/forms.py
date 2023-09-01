from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(forms.ModelForm):
    email = forms.CharField(
        min_length=6,
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
            }
        ),
    )
    username = forms.CharField(
        min_length=6,
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        ),
    )
    password = forms.CharField(
        min_length=6,
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        ),
    )
    password2 = forms.CharField(
        min_length=6,
        max_length=255,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Repeat password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("email", "username", "password", "password2")

    def clean(self):
        if (
            not self.cleaned_data["password"] == self.cleaned_data["password2"]
            or not self.cleaned_data["password2"]
        ):
            self._errors["password2"] = self.error_class(
                ["Password doesn't match"]
            )
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            self._errors["email"] = self.error_class(
                ["Such user with email alredy exists"]
            )
        return self.cleaned_data

    def save(self, commit=True):
        self.cleaned_data.pop("password2")
        return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.ModelForm):
    pass
