from django import forms
from django.forms import TextInput, Textarea, Select, CheckboxInput, RadioSelect

from .models import *


# Mobile phone category
class Adnew_Post(forms.ModelForm):

    class Meta:
        model = Mobile
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'model' : TextInput(attrs={'class':'form-control'}),
            'address' : TextInput(attrs={'class':'form-control'}),
            'phone_number' : TextInput(attrs={'class':'form-control'}),
            'price' : TextInput(attrs={'class':'form-control'}),
            'negotiable' : CheckboxInput(attrs={'class':'form-check-input'}),
            'description' : Textarea(attrs={'class':'form-control'}),
            'condition' : Select(attrs={'class':'form-control'}),
            'category' : Select(attrs={'class':'form-control'}),
            'division' : Select(attrs={'class':'form-control'}),
            'brand' : Select(attrs={'class':'form-control'}),
        }



# Education category
class Adnew_Post_Study(forms.ModelForm):

    class Meta:
        model = Study
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'address' : TextInput(attrs={'class':'form-control'}),
            'phone_number' : TextInput(attrs={'class':'form-control'}),
            'pay_per_month' : TextInput(attrs={'class':'form-control'}),
            'negotiable' : CheckboxInput(attrs={'class':'form-check-input'}),
            'description' : Textarea(attrs={'class':'form-control'}),
            'study_type' : Select(attrs={'class':'form-control'}),
            'category' : Select(attrs={'class':'form-control'}),
            'division' : Select(attrs={'class':'form-control'}),
        }


# Mobile Television category
class Adnew_television_Post(forms.ModelForm):

    class Meta:
        model = Television
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'inches' : TextInput(attrs={'class':'form-control'}),
            'address' : TextInput(attrs={'class':'form-control'}),
            'phone_number' : TextInput(attrs={'class':'form-control'}),
            'price' : TextInput(attrs={'class':'form-control'}),
            'negotiable' : CheckboxInput(attrs={'class':'form-check-input'}),
            'description' : Textarea(attrs={'class':'form-control'}),
            'condition' : Select(attrs={'class':'form-control'}),
            'category' : Select(attrs={'class':'form-control'}),
            'division' : Select(attrs={'class':'form-control'}),
            'brand' : Select(attrs={'class':'form-control'}),
        }





# Property Category
class Adnew_property_Post(forms.ModelForm):

    class Meta:
        model = Property
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'square_feed' : TextInput(attrs={'class':'form-control'}),
            'address' : TextInput(attrs={'class':'form-control'}),
            'phone_number' : TextInput(attrs={'class':'form-control'}),
            'price' : TextInput(attrs={'class':'form-control'}),
            'negotiable' : CheckboxInput(attrs={'class':'form-check-input'}),
            'description' : Textarea(attrs={'class':'form-control'}),
            'condition' : Select(attrs={'class':'form-control'}),
            'category' : Select(attrs={'class':'form-control'}),
            'division' : Select(attrs={'class':'form-control'}),
            'bed_room' : Select(attrs={'class':'form-control'}),
            'bath_room' : Select(attrs={'class':'form-control'}),
        }



# Computing category
class Adnew_computing_Post(forms.ModelForm):

    class Meta:
        model = Computing
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'model' : Select(attrs={'class':'form-control'}),
            'address' : TextInput(attrs={'class':'form-control'}),
            'phone_number' : TextInput(attrs={'class':'form-control'}),
            'price' : TextInput(attrs={'class':'form-control'}),
            'negotiable' : CheckboxInput(attrs={'class':'form-check-input'}),
            'description' : Textarea(attrs={'class':'form-control'}),
            'condition' : Select(attrs={'class':'form-control'}),
            'computing_type' : Select(attrs={'class':'form-control'}),
            'category' : Select(attrs={'class':'form-control'}),
            'division' : Select(attrs={'class':'form-control'}),
            'brand' : Select(attrs={'class':'form-control'}),
        }
