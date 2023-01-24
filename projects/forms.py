from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateJobpostForm(ModelForm):
    class Meta:
        model = postjob
        fields = '__all__'
        exclude = ['user']


class CreateFeedback(ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = company
        fields = '__all__'
        exclude = ['user']


class CandidateForm(ModelForm):
    class Meta:
        model = candidate
        fields = '__all__'
        exclude = ['user']


class ApplyForm(ModelForm):
    dob = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}), required=False)

    class Meta:
        model = applyforjob1
        fields = '__all__'
        exclude = ['candidate']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
