from django import forms
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from .models import resume_data,skills,experience,Education
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'type': "text",   'class': "form-control has-success has-feedback", 'name': "nm", 'placeholder': "eg. Josh Gordon",}),
            'email': forms.TextInput(attrs={'id': 'email','type': 'email',    'class': "form-control has-success has-feedback",'name':'email','placeholder': 'Email' }),
            'email2': forms.EmailInput(attrs={'type': 'email',   'class': "form-control has-success has-feedback",}),
            'password':forms.TextInput(attrs={'type': 'password','class': "form-control has-success has-feedback",}),
        }


    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
            
            
class resume_dataForm(ModelForm):
    class Meta:
        model = resume_data
        fields = ('FullName', 'Email', 'Phone', 'Profile', 'Profession','University','Address',)

        widgets = {
        'FullName': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "nm", 'placeholder': "eg. Josh Gordon"}),
        'Profession': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "position", 'placeholder': "Software Developer"}),
        'Phone': forms.NumberInput(attrs={'type': "number", 'class': "form-control has-success has-feedback", 'name': "ph", 'placeholder': "Number with country code"}),
        'Profile': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "proffile", 'placeholder': "Something about you!"}),
        'Email': forms.EmailInput(attrs={'type': "email", 'class': "form-control has-success has-feedback", 'name': "Eamil", 'placeholder': "abc@gmail.com"}),
        'University': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "col", 'placeholder': "eg : standford"}),
        'Address': forms.TextInput(attrs={'type':"text",'class':"form-control has-success has-feedback" ,'name':"ADDr" ,'placeholder':""}),
        }
    
class skillsForm(forms.ModelForm):
    
    class Meta:
        model = skills
        fields = ('Skills',)
        widgets = {
            'Skills': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "skills", 'placeholder': "eg. python,django"}),
        }
class experienceForm(forms.ModelForm):
    
    class Meta:
        model = experience
        fields = ('Heading','Post','From','To','Description',)
        widgets = {
            'Heading': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "nm", 'placeholder': "eg. Josh Gordon"}),
            'Post': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "position", 'placeholder': "Software Developer"}),
            'From': forms.DateInput(attrs={'type':'date','class':"form-control has-success has-feedback",'name':'from','placeholder':'06/06/2020'}),
            'To': forms.DateInput(attrs={'type': 'date', 'class': "form-control has-success has-feedback", 'name': 'To', 'placeholder': '06/06/2020'}),
            'Description': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "Desc", 'placeholder': ""}),
              }
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('School','Class','Cgpa','Passing_year',)
        widgets = {
            'School': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "sch", 'placeholder': " "}),
            'Class': forms.TextInput(attrs={'type': "text", 'class': "form-control has-success has-feedback", 'name': "cls", 'placeholder': "10th,12th,B-tech,"}),
            'Cgpa': forms.NumberInput(attrs={'type': "number", 'class': "form-control has-success has-feedback", 'name': "cgpa", 'placeholder': "7.6,8.5"}),
            'Passing_year': forms.NumberInput(attrs={'type': "number", 'class': "form-control has-success has-feedback", 'name': "Passing_year", 'placeholder': ""}),
        }
 
