from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
import base64
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from jobs.models import Job
from courses.models import Course
from django.contrib.auth.password_validation import validate_password, password_changed, password_validators_help_texts
from django.core.exceptions import ValidationError

User = get_user_model()
def signup(request):
    jobs = Job.objects
    courses=Course.objects
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', { 'error': 'username уже занят'})
            except User.DoesNotExist:
                try:
                    user=User.objects.get(email=request.POST['email'])
                    return render(request, 'accounts/signup.html', { 'error': 'email уже зарегистрирован'})
                except User.DoesNotExist:
                    errors={}
                    try:
                        validate_password(request.POST['password1'], user=None, password_validators=None)
                    except ValidationError as e:
                        errors['password1']=list(e.messages)
                    if errors:
                        return render(request, 'accounts/signup.html', { 'errorvalids': errors['password1'] })
                    else:
                        user=User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                        user.is_active = False
                        user.save()
                        current_site = get_current_site(request)
                        mail_subject = 'Активация вашей учетной записи.'
                        message = render_to_string('accounts/acc_active_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                        })
                        to_email = request.POST['email']
                        email = EmailMessage(
                                    mail_subject, message, to=[to_email]
                        )
                        email.send()
                        return render(request, 'accounts/login.html', { 'info': 'Спасибо за регистрацию! Проверьте пожалуйста вашу эелектронную почту, на нее выслано письмо подтверждения вашего email. После подтверждения вашего email вы сможете авторизоваться автоматически.'})
                # else:
                #     return render(request, 'accounts/signup.html', { 'error': django.core.exceptions.ValidationError})
                # auth.login(request, user)
                # return redirect('home')
        else:
            return render(request, 'accounts/signup.html', { 'error': 'Пароли должны совпадать'})
        #the user wants signup
    else:
        #the user wants enter info
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', { 'error': 'username или пароль не правильные!'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    #TODO need to route to Homepage
    return render(request, 'accounts/signup.html')

def activate(request, uidb64, token):
    jobs = Job.objects
    courses=Course.objects
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        # return redirect('home')
        return render(request, 'jobs/home.html', { 'info': 'Спасибо за подтверждение вашего email, теперь вы авторизованы на сайте!', 'jobs': jobs, 'courses': courses })
    else:
        return render(request, 'accounts/login.html', { 'info': 'Вы прошли по не валидной ссылке.'})

from django.shortcuts import render

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'accounts/user_profile.html', {"user":user})

# def passwordchange(request):
#     if request.method == 'POST':
#         user=User.objects.get(email=request.POST['email'])
#         current_site = get_current_site(request)
#         mail_subject = 'Сброс пароля'
#         message = render_to_string('accounts/passwordemail.html', {
#             'user': user,
#             'domain': current_site.domain,
#             'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
#             'token':account_activation_token.make_token(user),
#         })
#         to_email = request.POST['email']
#         email = EmailMessage(
#                     mail_subject, message, to=[to_email]
#         )
#         email.send()
#         return render(request, 'accounts/passwordchange.html', { 'info': 'Проверьте пожалуйста вашу эелектронную почту, на нее выслана ссылка на сброс пароля'})
#     else:
#         return render(request, 'accounts/passwordchange.html')
#
# def password(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         if request.method == 'POST':
#             if request.POST['password1'] == request.POST['password2']:
#                 user.set_password(request.POST['password1'])
#                 user.save()
#                 return render(request, 'jobs/home.html', { 'info': 'Вы успешно сменили пароль!', 'jobs': jobs, 'courses': courses })
#             else:
#                 return render(request, 'accounts/password.html', { 'info': 'Пароли не совпадают'})
#         else:
#             return render(request, 'accounts/pasword.html')
#     else:
#         return render(request, 'jobs/home.html', { 'info': 'Вы прошли по не валидной ссылке'})
