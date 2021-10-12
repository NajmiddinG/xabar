from django.contrib import messages
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .models import Message


def send(request):
    if request.POST:
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('toemail')
        from_email = request.POST.get('from_email')
        try:
            send_mail(subject, message, from_email, [f'{email}'])
            Message.objects.create(who=from_email, towhom=email, subject=subject, message=message)
            messages.success(request, "Xabaringiz jo'natildi")
        except BadHeaderError:
            return HttpResponse('Xatolik !!!')
    return render(request, 'index.html')