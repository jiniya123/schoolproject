from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile,Purpose,Course,Department

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    purpose = forms.ChoiceField(choices=[(purpose.id, purpose.name) for purpose in Purpose.objects.all()])

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError('Age cannot be negative.')
        return age

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label='Select Department'  # Add this line to provide an initial blank option
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        empty_label='Select Course'
    )

    class Meta:
        model = UserProfile
        fields = '__all__'