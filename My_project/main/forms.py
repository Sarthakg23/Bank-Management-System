from django import forms


from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'


class Userloginform(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['email','password']

class credit_form(forms.ModelForm):
    class Meta:
        model = models.Credit
        fields = '__all__'

class debit_form(forms.ModelForm):
    class Meta:
        model = models.Debit
        fields = '__all__'

class transfer_form(forms.ModelForm):
    class Meta:
        model = models.Transfer
        fields = '__all__'

class B_signup_form(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = '__all__'


class B_login_form(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['email_emp','password_emp']