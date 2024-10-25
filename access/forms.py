# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.translation import gettext_lazy as _

# class CustomLoginForm(AuthenticationForm):
#     username = forms.EmailField(label=_("Email"), max_length=254)

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if not username:
#             raise forms.ValidationError(_("Please enter a valid email."))
#         return username

# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.translation import gettext_lazy as _

# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(label=_("Email/Username"), max_length=254)

#     class Meta:
#         model = AuthenticationForm
#         fields = ('username', 'password')

# class EmailOrUsernameBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(
#                 models.Q(username=username) | models.Q(email=username)
#             )
#         except UserModel.DoesNotExist:
#             return None
#         if user.check_password(password):
#             return user
#         return None

from django import forms

class EmailForm(forms.Form):
    to = forms.EmailField(label='Destinatário')
    subject = forms.CharField(max_length=255, label='Assunto')
    body = forms.CharField(widget=forms.Textarea, label='Corpo')
    attachment = forms.FileField(required=False, label='Anexo')