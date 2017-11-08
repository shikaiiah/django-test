from django import forms
from django.forms import fields, widgets


class RegisterForm(forms.Form):
    username = fields.CharField(min_length=6, max_length=12,
                                label="username")
    password1 = fields.CharField(min_length=6, max_length=8,
                                 label="password 1",
                                 widget=widgets.PasswordInput)
    password2 = fields.CharField(min_length=6, max_length=8,
                                 label="password 2",
                                 widget=widgets.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(u"两次密码必须一致")
