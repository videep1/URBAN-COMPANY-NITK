from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage

# from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.contrib.sites.shortcuts import get_current_site
# from .utils import token_generator

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        #GET USER DATA
        messages.success(request, 'Success whatsapp')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context={
            'fieldValues':request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create_user(username = username, email = email)
                user.set_password(password)
                user.is_active = False
                user.save()

                #path to views
                # getting domain we are on
                # relative url to verification
                # encode uid
                # token
                # uidb64 = force_bytes(urlsafe_base64_encode(user.pk))
                # domain = get_current_site(request).domain
                # link = reverse('activate', kwargs={'uidb64':uidb64, 'token':token_generator.make_token(user)})
                email_subject = 'Activate your account'

                # activate_url = 'http://'+domain+link

                # email_body = 'Hi' +user.username + 'Please use this link to verify your account\n' +activate_url
                email_body = 'Activate account'


                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )
                email.send(fail_silently=False)
                messages.success(request, 'Account created successfully')
                return render(request, 'authentication/register.html')

        return render(request, 'authentication/register.html')


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry email in use,choose another one '}, status=409)
        return JsonResponse({'Email_valid': True})

# Create your views here.


# class VerificationView(View):
#     def get(self, request,uidb64, token):
#         return redirect('login')
