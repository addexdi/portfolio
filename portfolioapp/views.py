from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolioapp/index.html')


    from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib import messages
# from .forms import ContactForm

def index(request):
    return render(request, 'portfolioapp/index.html')


# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
        
#         if form.is_valid():
#             subject = form.cleaned_data.get('subject')
#             message = form.cleaned_data.get('content')
#             recipient = 'headofstate123@gmail.com'

#             send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently = False)
#             messages.success(request, 'Thanks for contacting me ')
            

#             if form.is_valid() == True:
#                 subject = 'Thanks for Contacting Me'
#                 message = 'I would reply to your message as soon as possible. From Olamilekan Azeez'
#                 receiver = form.cleaned_data.get('email')
#                 send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently = False)
#                 # messages.success(request, 'Thanks for contacting me')
#             return redirect('contact')

#     return render(request, 'resumeapp/index.html', {'form': form})