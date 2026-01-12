from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'occupation', 'company_name', 'location', 'website', 'about_me', 'project_description']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 11, 'cols': 110}),
        }
