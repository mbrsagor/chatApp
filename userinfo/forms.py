from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea, Select, RadioSelect, DateInput

from .models import *


# User Registeration Form
class UserRegisteration(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
        }





# Adding Total Service show homepage
class AddService(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'service_ulr' : TextInput(attrs={'class':'form-control'}),
        }



# Add Team Member
class AddTeam(forms.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'designation' : TextInput(attrs={'class':'form-control'}),
            'description' : TextInput(attrs={'class':'form-control'}),
        }




# Add  Custoamr Review
class AddReview(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'designation' : TextInput(attrs={'class':'form-control'}),
            'comments' : Textarea(attrs={'class':'form-control'}),
        }



# Add  Custoamr Review
class AddPricing(forms.ModelForm):

    class Meta:
        model = Pricing
        fields = '__all__'

        widgets = {
            'plane_name' : TextInput(attrs={'class':'form-control'}),
            'price' : TextInput(attrs={'class':'form-control'}),
            'colum1' : TextInput(attrs={'class':'form-control'}),
            'colum2' : TextInput(attrs={'class':'form-control'}),
            'colum3' : TextInput(attrs={'class':'form-control'}),
            'colum4' : TextInput(attrs={'class':'form-control'}),
            'colum5' : TextInput(attrs={'class':'form-control'}),
        }




# update profile Setting
class ProfileSetting(forms.ModelForm):

    class Meta:
        model = UpdateProfile
        fields = '__all__'

        widgets = {
            'full_name' : TextInput(attrs={'class':'form-control'}),
            'date_of_birth' : DateInput(attrs = {'class' : 'form-control'}),
            'gender' : Select(attrs = {'class' : 'form-control'}),
            'address' : TextInput(attrs = {'class' : 'form-control'}),
            'phone_number' : TextInput(attrs = {'class' : 'form-control'}),
            'profession' : TextInput(attrs = {'class' : 'form-control'}),
            'user_bio' : Textarea(attrs = {'class' : 'form-control'}),
        }



# Add  Custoamr Review
class ContactForm(forms.Form):
    # name = forms.CharField(required = True,  widget=forms.TextInput(attrs={'class': 'form-control input'}))
    from_email = forms.EmailField(required = True,  widget=forms.TextInput(attrs={'class': 'form-control input'}))
    subject = forms.CharField(required = True,  widget=forms.TextInput(attrs={'class': 'form-control input'}))
    message = forms.CharField(required = True,  widget=forms.Textarea(attrs={'class': 'form-control textarea'}))
