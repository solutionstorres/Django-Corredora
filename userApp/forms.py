from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class FormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['username'].widget.attrs['placeholder'] = 'Correo Electrónico'

class FormUsuario(forms.ModelForm):

    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control form-control-user',
            'placeholder': 'Contraseña',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Repetir Contraseña',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombre','apellido')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-user',
                    'placeholder': 'Nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Apellido',
                }                
            ),
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Usuario',
                }
            )
        }

    def clean_password2(self):
        """ Validación de Contraseña
        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.
        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormUsuarioFoto(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('imagen',)
        widgets = {
            'imagen': forms.FileInput(
                attrs = {
                    'class': 'form-control form-control-user',
                }
            )
        }