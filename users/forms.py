from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from users.functions import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    suite = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zipcode = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [ 'street', 'suite', 'city', 'zipcode', 'phone', 'website', 'company_name', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']


    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError("Lütfen en az 8 karakter uzunluğunda bir şifre giriniz.")
        elif len(password1) > 16:
            raise forms.ValidationError("Lütfen en fazla 16 karakter uzunluğunda bir şifre giriniz.")
        elif not buyuk_harf_var_mi(password1):
            raise forms.ValidationError("Lütfen en az bir adet büyük harf giriniz.")
        elif not kucuk_harf_var_mi(password1):
            raise forms.ValidationError("Lütfen en az bir adet küçük harf giriniz.")
        elif not ozel_karakter_var_mi(password1):
            raise forms.ValidationError("Lütfen en az bir adet özel karakter giriniz.")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Girdiğiniz şifreler eşleşmiyor.")
        return password2

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


from todos.models import Todo

class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_completed','date_line']

