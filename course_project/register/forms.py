from django import forms
from personal_page.models import Account


class RegForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'password', 'email', 'username']
    password = forms.CharField(
        widget=forms.PasswordInput,
    )
    conf_password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Enter same password.'}
    )

    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password') != self.cleaned_data.get('conf_password'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Passwords should be the same!')
        return self.cleaned_data