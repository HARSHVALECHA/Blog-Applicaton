from django import forms
from django.contrib.auth.models import User
from .models import *

class rform(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)

    email=forms.CharField(widget=forms.EmailInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)
    #profile_pic=forms.FileField(required=True)

    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput
                            (attrs={'class': 'form-control'}),
                            label="Confirm your password",
                            max_length=30,
                            required=True)
    

    def clean_username(self):
        uname=self.cleaned_data['username']
        try:
            match=User.objects.get(username=uname)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username already exists')
    
    class Meta:
        model=User
        fields=['username','email','password','confirm_password']
'''
class info_form(forms.ModelForm):
    class Meta:
        model=info
        fields=['title','description','pos']
    
'''
class info_form(forms.Form):
    
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Title','class':'form-control','style':'width:300px;'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Comment','rows': 4, 'cols': 50, 'style':'resize:none;width:300px;','class':'form-control'}))
    pos=forms.FileField(required=False)

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                                 max_length=100,
                                 required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                                 max_length=100,
                                 required=False)

    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),
                          max_length=30,
                          required=False) 

    location = forms.CharField(
        
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

    pic = forms.FileField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'location','pic' ]

class cmtform(forms.ModelForm):

    class Meta:

        model = comment

        fields = ['user_cmt']