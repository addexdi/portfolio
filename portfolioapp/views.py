from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def index(request):
    if request.method != 'POST':
        return render(request, 'portfolioapp/index.html')
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    content = request.POST['content']
    recipient = 'devolamilekan@gmail.com'

    send_mail(subject, content, settings.EMAIL_HOST_USER, [recipient], fail_silently = False)
    messages.success(request, 'Thanks for contacting me ')

# Sending the user a confirmation email
    if content == content:
        subject = 'Thanks for Contacting Me'
        message = 'Thanks for contacting me i will reply as soon as possible. From Olamilekan Azeez'
        receiver = email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently = False)

    return redirect('index')