from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Ja existe usuário com esse username') #Validação se ja existe username
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuario cadastrado!')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválidos')

@login_required(login_url="/account/login")
def plataforma(request):
  return HttpResponse('Plataforma')
    
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import EmailForm

def send_email_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            attachment = request.FILES.get('attachment')

            email = EmailMessage(subject, body, to=[user.email])
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)
            email.send()

            messages.success(request, f'E-mail enviado para {user.email}!')
            return redirect('admin:auth_user_changelist')  # Aqui, você pode mudar para o ID do usuário
    else:
        form = EmailForm()

    return render(request, 'admin/send_email.html', {'form': form, 'user': user})



# def send_email_view(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST, request.FILES)
#         if form.is_valid():
#             to = form.cleaned_data['to']
#             subject = form.cleaned_data['subject']
#             body = form.cleaned_data['body']
#             attachment = request.FILES.get('attachment')

#             email = EmailMessage(subject, body, to=[to])
#             if attachment:
#                 email.attach(attachment.name, attachment.read(), attachment.content_type)
#             email.send()

#             messages.success(request, 'E-mail enviado com sucesso!')
#             return redirect('admin:auth_user_changelist')  # Redireciona para a lista de usuários
#     else:
#         form = EmailForm()

#     return render(request, 'admin/send_email.html', {'form': form})
        