from django import forms
from .models import UserTable

class  UserSignUp(forms.ModelForm):

	class Meta:
		model=UserTable
		widgets = {'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),}
		fields=['name','password','email','mobile']
